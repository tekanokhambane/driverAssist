from rest_framework import serializers
from .models import Vehicle, Trailer


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = "__all__"
