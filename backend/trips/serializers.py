from rest_framework import serializers
from .models import Trip
from users.serializers import DriverSerializer
from shippers.serializers import ShipperSerializer
from vehicles.serializers import VehicleSerializer, TrailerSerializer


class TripSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    shipper = ShipperSerializer()
    vehicle = VehicleSerializer()
    trailer = TrailerSerializer()

    class Meta:
        model = Trip
        fields = "__all__"
