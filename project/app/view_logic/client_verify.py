from django.shortcuts import render
from django.http import JsonResponse
from app.models import UnverifiedClient, Client
class ClientVerify():
    def get(self, request):
        """Client verify API view logic for handling GET requests"""
        try:
            contextDict = {}
            contextDict['id'] = request.query_params['id']
            if not contextDict['id']:
                raise Exception()
            contextDict['unverifiedClient'] = UnverifiedClient.objects.get(nonce=contextDict['id'])
        except Exception as e:
            print(e)
        finally:
            return render(request, 'client_verify.html', context=contextDict)

    def post(self, request):
        """Client verify API view logic for handling POST requests"""
        try:
            response = {'result': False}
            body = request.data
            client = Client.objects.get(pk=int(body['client']))
            unverifiedClient = UnverifiedClient.objects.get(client=client)
            unverifiedClient.delete()
            client.firstName = body['firstName']
            client.lastName = body['lastName']
            client.address = body['address']
            client.newsletter = body['newsletter']
            client.verified = True
            client.save()
            response['result'] = True
        except Exception as e:
            print(e)
            response['result'] = False
        finally:
            return JsonResponse(response)
