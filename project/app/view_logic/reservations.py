from django.http import JsonResponse
from rest_framework.response import Response
from app.serializers import ReservationSerializer, LocationSerializer
from app.models import Reservation, Location, Client
from app.src.errors import OutstandingReservationExists
from app.src.nonce import nonce

class Reservations():
    """GET/POST view logic of reservations API view"""
    def get(self, request):
        """Reservation API view logic for retrieving reservations matching query criteria"""

        query_set = dict((k, v) for k, v in request.query_params.items())
        reservation_objects = Reservation.objects.filter(**query_set).filter(cancelled=False)
        serializer = ReservationSerializer(reservation_objects, many=True)
        location = False
        if query_set['location']:
            location = LocationSerializer(Location.objects.get(pk=int(query_set['location']))).data
        return Response({'reservations': serializer.data, 'location': location})

    def post(self, request):
        """Reservation API view logic for creating new reservations"""
        print('creating reservation')
        body = request.data
        responseData = {
            'result': True,
            'message': 'Reservation created successfully!'
        }
        try:
            if not Reservation.reservationAvailable(date=body['date'], time=body['time'], location=body['location']):
                raise OutstandingReservationExists() 
            result_tuple = Client.objects.get_or_create(email=body['email'])
            client = result_tuple[0]
            desiredLocation = Location.objects.get(pk=int(body['location']))
            newReservation = Reservation.objects.create(date=body['date'], time=body['time'], client=client, location=desiredLocation, requests=body['requests'], confirmation_nonce=nonce(12))
            newReservation.save()
            responseData['result'] = Client.sendReservationConfirmation(client, newReservation)
            if not responseData['result']:
                raise Exception()
            print('reservation created')
        except Location.DoesNotExist as e:
            responseData['message'] = 'Invalid location'
            responseData['result'] = False
        except OutstandingReservationExists as e:
            responseData['message'] = 'Reservation already exists'
            responseData['result'] = False
        except Exception as e:
            print(e)
            responseData['message'] =  'Something went wrong'
            responseData['result'] = False
        finally:
            return Response(responseData)