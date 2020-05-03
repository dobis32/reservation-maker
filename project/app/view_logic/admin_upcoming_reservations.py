from django.shortcuts import render
from django.http import JsonResponse
from app.models import Reservation
from app.serializers import ReservationSerializer

class AdminUpcomingReservations():
    """API View logic for admin login"""
    def get(self, request):
        contextData = {}
        print(request.query_params['end'])
        query_set = Reservation.objects.order_by('date').filter(date__gte=request.query_params['start']).filter(date__lte=request.query_params['end']).values('date').distinct()
        reservationDates = []
        print(query_set)
        for element in query_set:
            date = element['date']
            reservation = {'date': date}
            reservation['reservations'] = Reservation.objects.filter(date=date)
            reservationDates.append(reservation)
        contextData['reservationDates'] = reservationDates
        return render(request, 'admin_upcoming_reservations.html', context=contextData)

    def post(self, request):
        return JsonResponse({'result': True})