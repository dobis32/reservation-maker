"""Django Models"""
from django.db import models
from django.core.validators import MinValueValidator, validate_email
from app.validators import reservationTimeValidator, reservationDateValidator
from app import sendgrid as send_grid_py
from app.nonce import nonce

# Create your models here.
class Admin(models.Model):
    """Admin data model"""
    username = models.CharField(max_length=24, null=False, default="admin")
    password = models.CharField(max_length=256, null=False)
    email = models.EmailField(unique=True, null=False, validators=[validate_email])
    
class Client(models.Model):
    """Client data model"""
    firstName = models.CharField(max_length=24, blank=True, null=True)
    lastName = models.CharField(max_length=24, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(validators=[validate_email], unique=True)
    verified = models.BooleanField(default=False)
    @classmethod
    def sendReservationConfirmation(self, client, reservation):
        n = nonce(12)
        if client.verified:
            # send reservation confirmation
            return send_grid_py.sendReservationConfirmation(nonce=n, email_to=client.email)
        else:
            # send request for client info
            unverifiedClient = UnverifiedClient.objects.create(nonce=n, client=client, reservation=reservation)
            unverifiedClient.save()
            return send_grid_py.sendClientVerification(nonce=n, email_to=client.email)

class Location(models.Model):
    """Location data model"""
    contact = models.CharField(max_length=24)
    address = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

class Reservation(models.Model):
    """Reservation data model"""
    time = models.CharField(max_length=8, validators=[reservationTimeValidator])
    date = models.CharField(max_length=9, validators=[reservationDateValidator])
    requests = models.CharField(max_length=256, default="None")
    client = models.ForeignKey(Client, models.CASCADE)
    location = models.ForeignKey(Location, models.SET('TBD'))
    verified = models.BooleanField(default=False)
    @classmethod
    def reservationAvailable(self, date, time, location):
        try:
            reservation = self.objects.get(date=date, time=time, location=int(location))
            return False
        except Reservation.DoesNotExist as e:
            return True
        except Exception:
            return False

class UnverifiedClient(models.Model):
    """Unverified clients data model"""
    nonce = models.CharField(max_length=256, null=False)
    reservation = models.ForeignKey(Reservation, models.CASCADE)
    client = models.ForeignKey(Client, models.CASCADE)
