from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
import os
import jwt
import datetime
class AdminLogin():
    """API View logic for admin login"""
    def get(self, request):
        """Logic for handling GET requests to admin logic API view"""
        return render(request, 'admin_login.html')

    def post(self, request):
        """Logic for handling POST requests to admin logic API view"""
        try:
            response = {'result': True}
            body = request.data
            user = authenticate(username=body['username'], password=body['password'])
            if not user:
                raise Exception()

            formatttedExpiration =(datetime.datetime.utcnow() + datetime.timedelta(minutes=30)).isoformat()
            headers = {'exp': formatttedExpiration}
            response['token'] = str(jwt.encode({'username': body['username'], 'password': body['password']}, os.environ.get('JWT_SECRET'), algorithm='HS256', headers=headers))[1:].replace("'", "")
        except Exception as e:
            print(e)
            response['result'] = False
        finally:
            return JsonResponse(response)