from django.db import models


# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.brand + ' ' + self.car_model


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.car.brand + ' ' + self.car.car_model + ' ' + str(self.start_date) + ' - ' + str(
            self.end_date) + ' ' + self.contact_email

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    bookings = models.ManyToManyField(Booking)

    def __str__(self):
        return self.username + ' ' + self.email