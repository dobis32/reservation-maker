"""Django Views"""
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Reservation, Location
from app.serializers import ReservationSerializer, LocationSerializer

# Create your views here.

class Index(View):
    """API View for Index"""
    def get(self, request):
        """Handle GET requests"""
        locations = LocationSerializer(Location.objects.all(), many=True).data
        times = [
            {'available': True, 'id': 'T9-00-AM', 'label': '9:00 AM'},
            {'available': True, 'id': 'T9-30-AM', 'label': '9:30 AM'},
            {'available': True, 'id': 'T10-00-AM', 'label': '10:00 AM'},
            {'available': True, 'id': 'T10-30-AM', 'label': '10:30 AM'},
            {'available': True, 'id': 'T11-00-AM', 'label': '11:00 AM'},
            {'available': True, 'id': 'T11-30-AM', 'label': '11:30 AM'},
            {'available': True, 'id': 'T12-00-PM', 'label': '12:00 PM'},
            {'available': True, 'id': 'T12-30-PM', 'label': '12:30 PM'},
            {'available': True, 'id': 'T1-00-PM', 'label': '1:00:PM'},
            {'available': True, 'id': 'T1-30-PM', 'label': '1:30 PM'},
            {'available': True, 'id': 'T2-00-PM', 'label': '2:00 PM'},
            {'available': True, 'id': 'T2-30-PM', 'label': '2:30 PM'},
            {'available': True, 'id': 'T3-00-PM', 'label': '3:00 PM'},
            {'available': True, 'id': 'T3-30-PM', 'label': '3:30 PM'},
            {'available': True, 'id': 'T4-00-PM', 'label': '4:00 PM'},
            {'available': True, 'id': 'T4-30-PM', 'label': '4:30 PM'},
        ]
        return render(request, 'index.html', context={'times': times, 'available_locations': locations})

class Reservations(APIView):
    """API View for Reservations Model"""

    def get(self, request):
        """Handle GET requests"""
        query_set = dict((k, v) for k, v in request.query_params.items())
        reservation_objects = Reservation.objects.filter(**query_set)
        serializer = ReservationSerializer(reservation_objects, many=True)
        location = False
        if query_set['location']:
            location = LocationSerializer(Location.objects.get(pk=int(query_set['location']))).data
        return Response({'reservations': serializer.data, 'location': location})

    def post(self, request):
        """Handle POST requests"""
        body = request.data
        print('body', body)
        return Response('poop')
