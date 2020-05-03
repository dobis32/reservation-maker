from django.shortcuts import render
from django.http import JsonResponse
from app.serializers import ReservationSerializer
from app.models import Reservation, Admin
from app.src.todayString import getTodayString
from datetime import datetime
class AdminDashboard():

    def get(self, request):
        contextData = {}
        date = request.GET.get('today', None)   
        print(date)
        if not date:
            date = getTodayString()

        print(date)             
        contextData['reservations'] = {}
        contextData['reservations']['today'] = Reservation.objects.filter(date__gte=date).filter(date__lte=date).filter(cancelled=False).count()
        contextData['reservations']['new'] = Reservation.objects.filter(date__gte=date).filter(cancelled=False).filter(notify_admin=True).count()
        contextData['reservations']['cancelled'] = Reservation.objects.filter(cancelled=True).filter(notify_admin=True).count()
        contextData['todayDate'] = date
        return render(request, 'admin_dashboard.html', context=contextData)
    
    def post(self, request):
        try:
            response = {}
            response['result'] = True
            response['message'] = 'Not yet implemented.'
        except Exception as e:
            print(e)
            response['result'] = False
            response['message'] = str(e)
        finally:
            return JsonResponse(response)

        