from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Booking(models.Model):
    Booking_ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    BookingDate = models.DateField()

    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    Menu_ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return self.Title