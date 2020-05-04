from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import Reservation
import ast

class ReservationReview():
    def get(self, request):
        try:
            nonce = request.GET.get('reservation', False)
            if not nonce:
                raise Exception('missing reservation nonce')
            reservation = Reservation.objects.get(confirmation_nonce=nonce)
            contextData = {'reservation': reservation}
            return render(request, 'reservation_review.html', context=contextData)
        except Exception as e:
            print(e)
            return redirect('resource_404')

    def delete(self, request):
        responseData = {}
        try:
            s = str(request.read()).split("'")[1]
            body = ast.literal_eval(s)
            nonce = body['reservation']
            if not nonce:
                raise Exception('missing reservation nonce')
            reservationToDelete = Reservation.objects.get(confirmation_nonce=nonce)
            reservationToDelete.delete()
            responseData['result'] = True
        except Exception as e:
            print(e)
            responseData['result'] = False
            responseData['message'] = str(e)
        finally:
            return JsonResponse(responseData)
        
        
    def put(self, request):
        s = str(request.read()).split("'")[1]
        body = ast.literal_eval(s)
        return JsonResponse({'result': True, 'message': 'ding dong :^)'})
          
        
       