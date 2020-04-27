"""Django Serializers"""
from rest_framework import serializers
from app.models import Reservation, Location, Client

class ReservationSerializer(serializers.ModelSerializer):
    """Reservation model serializer"""
    class Meta:
        model = Reservation
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    """Location model serializer"""
    class Meta:
        model = Location
        fields = '__all__'
       
class ClientSerializer(serializers.ModelSerializer):
    """Client model serializer"""
    class Meta:
        model = Client
        fields = '__all__'
       