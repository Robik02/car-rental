from django.contrib import admin
from .models import Car, Booking, User

# Register your models here.
admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(User)