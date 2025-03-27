from django.db import models
from users.models import Driver
from vehicles.models import Vehicle


class Trip(models.Model):
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, related_name="driver_trips"
    )
    co_driver = models.ForeignKey(
        Driver, null=True, on_delete=models.SET_NULL, related_name="co_driver_trips"
    )
    shipper = models.ForeignKey(
        "shippers.Shipper", on_delete=models.CASCADE, related_name="shippments"
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    trailer = models.ForeignKey(
        "vehicles.Trailer", null=True, on_delete=models.SET_NULL
    )
    start_location = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    distance_travelled = models.FloatField(help_text="Distance in kilometers")
    total_duration = models.DurationField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.driver} - {self.start_location} to {self.dropoff_location}"
