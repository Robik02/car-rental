from django.urls import path
from .views import CarListView, BookingListView

urlpatterns = [
    path('api/cars/', CarListView.as_view(), name='car-list'),
    path('api/bookings/', BookingListView.as_view(), name='booking-list'),
]
