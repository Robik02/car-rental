from rest_framework import serializers
from .models import Car, Booking, User


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'