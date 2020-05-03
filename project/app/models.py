"""Django Models"""
from django.db import models
from django.core.validators import MinValueValidator, validate_email
from app.src.validators import reservationTimeValidator, reservationDateValidator
from app.src.errors import PasswordDoesNotMatch
from app.src import sendgrid as send_grid_py
from app.src.nonce import nonce
import jwt

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
    email = models.EmailField(validators=[validate_email], unique=True, null=True)
    verified = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)
    @classmethod
    def sendReservationConfirmation(self, client, reservation):
        """Send reservation confirmation email to client or send client verification email if client is not verified"""
        if client.verified:
            # send reservation confirmation
            n = nonce(12)
            return send_grid_py.sendReservationConfirmation(nonce=n, email_to=client.email)
        else:
            # send request for client info
            result_tuple = UnverifiedClient.objects.get_or_create(client=client)
            unverifiedClient = result_tuple[0]
            if(result_tuple[1]):
                n = nonce(12)
                unverifiedClient.nonce = n
                unverifiedClient.reservation = reservation
                unverifiedClient.save()
            return send_grid_py.sendClientVerification(nonce=unverifiedClient.nonce, email_to=client.email)

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
    cancelled = models.BooleanField(default=False)
    notify_admin = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)
    confirmation_nonce = models.CharField(max_length=256, null=True)
    @classmethod
    def reservationAvailable(self, date, time, location):
        """Check if reservation exists already"""
        try:
            reservation = self.objects.get(date=date, time=time, location=int(location), cancelled=False)
            return False
        except Reservation.DoesNotExist as e:
            return True
        except Exception:
            return False

class UnverifiedClient(models.Model):
    """Unverified clients data model"""
    nonce = models.CharField(max_length=256, null=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
