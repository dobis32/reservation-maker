from django.shortcuts import render
from app.serializers import LocationSerializer
from app.models import Location
class Index():
    def get(self, request):
        """Index API view logic for handling GET requests"""
        locations = LocationSerializer(Location.objects.all(), many=True).data
        times = [
            {'available': True, 'id': 'T9-00-AM', 'label': '9:00 AM'},
            {'available': True, 'id': 'T9-30-AM', 'label': '9:30 AM'},
            {'available': True, 'id': 'T10-00-AM', 'label': '10:00 AM'},
            {'available': True, 'id': 'T10-30-AM', 'label': '10:30 AM'},
            {'available': True, 'id': 'T11-00-AM', 'label': '11:00 AM'},
            {'available': True, 'id': 'T11-30-AM', 'label': '11:30 AM'},
            {'available': True, 'id': 'T12-00-PM', 'label': '12:00 PM'},
            {'available': True, 'id': 'T12-30-PM', 'label': '12:30 PM'},
            {'available': True, 'id': 'T1-00-PM', 'label': '1:00:PM'},
            {'available': True, 'id': 'T1-30-PM', 'label': '1:30 PM'},
            {'available': True, 'id': 'T2-00-PM', 'label': '2:00 PM'},
            {'available': True, 'id': 'T2-30-PM', 'label': '2:30 PM'},
            {'available': True, 'id': 'T3-00-PM', 'label': '3:00 PM'},
            {'available': True, 'id': 'T3-30-PM', 'label': '3:30 PM'},
            {'available': True, 'id': 'T4-00-PM', 'label': '4:00 PM'},
            {'available': True, 'id': 'T4-30-PM', 'label': '4:30 PM'},
        ]
        return render(request, 'index.html', context={'times': times, 'available_locations': locations})