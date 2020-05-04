from django.shortcuts import render
from django.http import JsonResponse
from app.models import Client

class AdminClients():
    def get(self, request):
        client_pk = request.GET.get('client', False)
        if client_pk:
            contextData = {}
            client = Client.objects.get(pk=int(client_pk))
            contextData['client'] = client
            return render(request, 'admin_client_view.html', context=contextData)

        else:
            contextData = {}
            clients = Client.objects.all()
            contextData['clients'] = clients
            return render(request, 'admin_clients.html', context=contextData)
