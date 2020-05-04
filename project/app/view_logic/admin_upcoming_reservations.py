from django.shortcuts import render
from django.http import JsonResponse
from app.models import Reservation
from app.serializers import ReservationSerializer

class AdminUpcomingReservations():
    """API View logic for admin login"""
    def get(self, request):
        contextData = {}
        query_set = Reservation.objects.order_by('date').filter(date__gte=request.query_params['start'])
        count = Reservation.objects.filter(date__gte=request.query_params['start'])
        query_set = query_set.filter(date__lte=request.query_params['end'])
        count = count.filter(date__lte=request.query_params['end'])
        query_set = query_set.filter(cancelled=False)
        count = count.filter(cancelled=False)
        query_set = query_set.values('date').distinct()
        count = count.count()
        if not count:
            contextData['noReservations'] = True
        reservationDates = []
        for element in query_set:
            date = element['date']
            reservation = {'date': date}
            reservation['reservations'] = Reservation.objects.filter(date=date).filter(cancelled=False)
            reservationDates.append(reservation)
        contextData['reservationDates'] = reservationDates
        return render(request, 'admin_upcoming_reservations.html', context=contextData)

    def post(self, request):
        return JsonResponse({'result': True})