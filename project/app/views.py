"""Django Views"""
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from app.view_logic.index import Index
from app.view_logic.reservations import Reservations
from app.view_logic.client_verify import ClientVerify
from app.view_logic.reservation_confirmation import ReservationConfirmation
from app.view_logic.admin_login import AdminLogin
from app.view_logic.admin_dashboard import AdminDashboard
from app.view_logic.admin_upcoming_reservations import AdminUpcomingReservations
from app.view_logic.admin_reservations import AdminReservations
from app.view_logic.admin_cancellations import AdminCancellations
from app.src.validators import adminValidator
from app.models import Reservation
import ast

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
    """API View for Admin login"""
    logic = AdminLogin()
    def get(self, request):
        """Handle GET requests"""
        return self.logic.get(request)

    def post(self, request):
        """Handle POST requests"""
        return self.logic.post(request)

class reservation_confirm(APIView):
    """API View for Reservation confirmations"""
    logic = ReservationConfirmation()
    def get(self, request):
        return self.logic.get(request)

    def post(self, request):
        return self.logic.post(request)

class admin_dashboard(APIView):
    """API View for Admin dashboard"""
    logic = AdminDashboard()
    def get(self, request):
        return self.logic.get(request)

    def post(self, request):
        return self.logic.post(request)

class admin_upcoming_reservations(APIView):
    """API View for upcoming reservations"""
    logic = AdminUpcomingReservations()
    def get(self, request):
        return self.logic.get(request)

    def post(self, request):
        return self.logic.post(request)

class admin_reservations(APIView):
    """API View for reservations management"""
    logic = AdminReservations()
    def get(self, request):
        return self.logic.get(request)

    def post(self, request):
        return self.logic.post(request)

    def delete(self, request):
        return self.logic.delete(request)

    def put(self, request):
        return self.logic.put(request)

class admin_cancellations(APIView):
    """API View for cancelled-reservations management"""
    logic = AdminCancellations()
    def get(self, request):
        return self.logic.get(request)

@api_view(['PUT'])
def dismiss_notification(request):
    s = str(request.read()).split("'")[1]
    body = ast.literal_eval(s)
    reservation = Reservation.objects.get(pk=body['id'])
    reservation.notify_admin = False
    reservation.save()
    return JsonResponse({'result': True})

@api_view(['POST'])
def verify_admin(request):
    try:
        response = {'result': True}
        oldToken = request.data['token']
        if not oldToken:
            raise Exception()
        token = adminValidator(oldToken)
        if not token:
            raise Exception()
        response['token'] = token
    except Exception:
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

@api_view(['GET'])
def redirect_to_admin_login(request):
    """View for redirecting to admin login page"""
    return redirect('admin_login')
