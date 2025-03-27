from django.db import models
from users.models import Driver


class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.make} {self.model} - {self.plate_number}"


class Trailer(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.make} {self.model} - {self.plate_number}"
