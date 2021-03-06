from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from app.models import Reservation
from app.src.todayString import getTodayString
import ast
class AdminReservations():

    def get(self, request):
        contextData = {}
        todayString = getTodayString()
        query_set = Reservation.objects.order_by('date').values('date').distinct().filter(date__gte=todayString)
        count = Reservation.objects.filter(date__gte=todayString).filter(cancelled=False)
        query_set = query_set.filter(cancelled=False)
        if request.GET.get('notify_admin', 'False') == 'True':
            count = count.filter(date__gte=todayString)
            query_set = query_set.filter(notify_admin=True)
        if request.GET.get('unconfirmed', 'True') == 'False':
            count = count.filter(date__gte=todayString)
            query_set = query_set.filter(confirmed=True)
        reservationDates = []
        count = count.count()
        if not count:
            contextData['noReservations'] = True
        for element in query_set:
            print(element)
            date = element['date']
            reservationDate = {'date': date}
            reservations = Reservation.objects.filter(date=date)
            if request.GET.get('notify_admin', 'False') == 'True':
                reservations = reservations.filter(notify_admin=True)
            if request.GET.get('unconfirmed', 'True') == 'False':
                reservations = reservations.filter(confirmed=True)

            reservationDate['reservations'] = reservations.order_by('time')
            reservationDates.append(reservationDate)
        contextData['reservationDates'] = reservationDates
        contextData['notify_admin'] = request.GET.get('notify_admin', False)
        contextData['unconfirmed'] = request.GET.get('unconfirmed', False)

        return render(request, 'admin_reservations.html', context=contextData)

    def post(self, request):
        return JsonResponse({'message': 'ding dong :^)'})

    def delete(self, request):
        s = str(request.read()).split("'")[1]
        body = ast.literal_eval(s)
        return JsonResponse({'message': 'ding dong :^)'})

    def put(self, request):
        return JsonResponse({'message': 'ding dong :^)'})
        

        

