from django.shortcuts import render
from rest_framework import generics
from .models import Car, Booking, User
from .serializers import CarSerializer, BookingSerializer, UserSerializer


# Create your views here.

# GET /api/cars
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# GET /api/bookings
class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# GET /api/users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
