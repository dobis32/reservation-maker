from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import Reservation

class ReservationConfirmation():
    """GET/POST logic for 'reservation confirm' view"""
    def get(self, request):
        """Render confirmation page for reservation with pk corresponding to GET query"""
        try:
            n = request.query_params['reservation']
            if not n:
                raise Exception()
            reservation = Reservation.objects.get(confirmation_nonce=n)
            return render(request, 'reservation_confirm.html', context={'reservation': reservation})
        except Exception as e:
            print(e)
            return redirect('index')


    def post(self, request):
        """Confirm reservation"""
        try:
            response = {'result' : False}
            id = request.data['id']
            if not id:
                raise Exception('Missing ID')
            reservation = Reservation.objects.get(pk=int(id))
            reservation.confirmed = True
            reservation.save()
            reservation.sendReservationLink(reservation.confirmation_nonce, reservation.client.email)
            response['result'] = True
        except Exception as e:
            print('error', e)
            response['result'] = False
        finally:
            return JsonResponse(response)