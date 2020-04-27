"""Django Views"""
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import ReservationSerializer, LocationSerializer, ClientSerializer
from app.errors import OutstandingReservationExists
from app.models import Reservation
from rest_framework.decorators import api_view
from app.view_logic.index import Index
from app.view_logic.reservations import Reservations
from app.view_logic.client_verify import ClientVerify

# Create your views here.

class Index(View):
    """API View for Index"""
    logic = Index()
    def get(self, request):
        """Handle GET requests"""
        return self.logic.get(request)

class Reservations(APIView):
    """API View for Reservations Model"""
    logic = Reservations()
    def get(self, request):
        """Handle GET requests"""
        return self.logic.get(request)

    def post(self, request):
        """Handle POST requests"""
        return self.logic.post(request)

class client_verify(APIView):
    """API View for Client confirmations"""
    logic = ClientVerify()
    def get(self, request):
        """Handle GET requests"""
        return self.logic.get(request)
    def post(self, request):
        """Handle POST requests"""
        return self.logic.post(request)

class admin_login(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

@api_view(['POST'])
def reservation_confirm(request):
    """API View for Reservation confirmations"""
    print('reservation confirmation', request)
    try:
        response = {}
        body = request.data
        print(request.data)
        reservation = Reservation.objects.get(pk=int(body['id']))
        reservation.verified = True
        reservation.save()
        response['result'] = True
    except Exception as e:
        print(e)
        response['result'] = False
    finally:
        return JsonResponse(response)

@api_view(['GET'])
def reservation_confirm_success(request):
    contextData = {}
    try:
        contextData['reservation'] = Reservation.objects.get(pk=int(request.query_params['id']))
        return render(request, 'reservation_confirm_success.html', context=contextData)
    except Exception as e:
        print('ERROR', e)
        return redirect('resource_404')
    
    

@api_view(['GET'])
def reservation_scheduled(request):
    """API View for successful Reservation booking"""
    return render(request, 'reservation_scheduled.html')

@api_view(['GET'])
def resource_404(request):
    """View for successful Reservation booking"""
    return render(request, '404_missing.html')

