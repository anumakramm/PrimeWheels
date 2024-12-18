from django.contrib import admin
from django.db import models
from .models import CarType, Vehicle, Buyer, OrderVehicle, LabMember, Feature

admin.site.register(CarType) 
admin.site.register(Vehicle) 
admin.site.register(Buyer) 
admin.site.register(OrderVehicle)
admin.site.register(LabMember)
admin.site.register(Feature)