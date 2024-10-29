from django.urls import path
from .views import CarListView, BookingListView, UserListView

urlpatterns = [
    path('api/cars/', CarListView.as_view(), name='car-list'),
    path('api/bookings/', BookingListView.as_view(), name='booking-list'),
    path('api/users/', UserListView.as_view(), name='user-list'),
]
