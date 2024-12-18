from django.db import models
from django.contrib.auth.models import User

class CarType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    car_type = models.ForeignKey(CarType, related_name='vehicles', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_description = models.TextField(null=True, blank=True)
    car_price = models.DecimalField(max_digits=10, decimal_places=4)
    inventory = models.PositiveIntegerField(default=10)
    instock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.car_type} {self.car_name}"
    
class Buyer(User):
    AREA_CHOICES = [
        ('W', 'Windsor'),
        ('LS', 'LaSalle'),
        ('A', 'Amherstburg'),
        ('L', 'Lakeshore'),
        ('LE', 'Leamington'),
        ('C', 'Chatham-Kent'),
        ('T', 'Toronto'),
        ('WL', 'Waterloo'),
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='C')
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    interested_in = models.ManyToManyField(CarType)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class OrderVehicle(models.Model):
    ORDER_STATUS_CHOICES = [
        (0, 'Successful'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
        (4, 'Cancelled'),
    ]

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.PositiveIntegerField(choices=ORDER_STATUS_CHOICES, default=1)

    def total_price(self):
        return self.quantity * self.vehicle.car_price

    def __str__(self):
        return f"{self.buyer} {self.vehicle} {self.quantity} {self.order_date} {self.order_status}"
    
class LabMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    personal_page = models.URLField(max_length=200)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"