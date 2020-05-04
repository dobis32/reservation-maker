from django.shortcuts import render
from django.http import JsonResponse
from app.models import Reservation
from app.src.todayString import getTodayString
class AdminCancellations():
    def get(self, request):
        today = getTodayString()
        contextData = {}
        cancelledReservations = []
        distinctDates = Reservation.objects.filter(date__gte=today).filter(cancelled=True)
        if request.GET.get('notify_admin', 'False') == 'True':
            distinctDates = distinctDates.filter(notify_admin=True)
        distinctDates.values('date').distinct().order_by('date')
        for d in distinctDates:
            cancellationDate = {}
            cancellationDate['date'] = d.date
            cancellations = Reservation.objects.filter(date=d.date).filter(cancelled=True)
            if request.GET.get('notify_admin', 'False') == 'True':
                cancellations = cancellations.filter(notify_admin=True)
            cancellationDate['cancellations'] = cancellations
            cancelledReservations.append(cancellationDate) 
        contextData['cancelledReservations'] = cancelledReservations
        count_query = Reservation.objects.filter(date__gte=today).filter(cancelled=True)
        if request.GET.get('notify_admin', 'False') == 'True':
            count_query = count_query.filter(notify_admin=True)
        count = count_query.count()
        if not count:
            contextData['noCancellations'] = True
        return render(request, 'admin_cancellations.html', context=contextData)

    def put(self, request):
        responseData = {}
        try:
            s = str(request.read()).split("'")[1]
            body = ast.literal_eval(s)
            reservationToCancel = Reservation.objects.get(nonce=body['cancel'])
            reservationToCancel.cancelled = True
            reservationToCancel.notify_admin = True
            reservationToCancel.save()
            reservation['result'] = True
        except Exception as e:
            print(e)
            responseData['result'] = False
            responseData['message'] = str(e)
        finally:
            return JsonResponse(responseData)

        
