from django.db import models
from django.core.validators import MinValueValidator, validate_email
from app.validators import reservationTimeValidator, reservationDateValidator

# Create your models here.
class Client(models.Model):
    firstName = models.CharField(max_length=24)
    lastName = models.CharField(max_length=24)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    address = models.CharField(max_length=256)
    email = models.EmailField(validators=[validate_email], unique=True)
    verified = models.BooleanField(default=False)

class Location(models.Model):
    contact = models.CharField(max_length=24)
    address = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

class Reservation(models.Model):
    time = models.CharField(max_length=8, validators=[reservationTimeValidator])
    date = models.CharField(max_length=9, validators=[reservationDateValidator])
    client = models.ForeignKey(Client, models.CASCADE)
    location = models.ForeignKey(Location, models.SET('TBD'))
