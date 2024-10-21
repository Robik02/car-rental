from django.shortcuts import render
from rest_framework import generics
from .models import Car, Booking
from .serializers import CarSerializer, BookingSerializer


# Create your views here.

# GET /api/cars
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# GET /api/bookings
class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
