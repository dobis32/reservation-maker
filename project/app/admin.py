from django.contrib import admin
from app.models import Client, Location, Reservation, UnverifiedClient

# Register your models here.
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Reservation)
admin.site.register(UnverifiedClient)
