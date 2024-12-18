from django.http import HttpResponse
from .models import CarType, Vehicle, LabMember
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from django.urls import path
from django.views.generic import ListView
# def homepage(request):
#     cartype_list = CarType.objects.all().order_by('id')
#     cars_list = Vehicle.objects.all().order_by('-car_price')
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types of Cars:' + '</p>'
#     heading2 = '<p>' + 'Different Cars:' + '</p>'
#     # response.write(heading1)
#     response.write(heading2)
#     # for cartype in cartype_list:
#     #     para = '<p>' + str(cartype.id) + ': ' + str(cartype) + '</p>'
#     #     response.write(para)
#     for car in cars_list[:10]:
#         para = '<p>' + str(car.id) + ': ' + str(car) + ' - ' + str(int(car.car_price)) + '</p>'
#         response.write(para)
#     return response

def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    return render(request, 'primewheelsapp/homepage.html', {'cartype_list': cartype_list})

def aboutus(request):
    return render(request, 'primewheelsapp/aboutus.html')

# def aboutus(request):
#     response = HttpResponse()
#     heading = '<p>' + 'About Us:' + '</p>'
#     para = '<p>' + 'We are a car dealership company that sells a variety of cars.' + '</p>'
#     response.write(heading)
#     response.write(para)
#     return response

def cardetail(request, cartype_no):
    cartype = get_object_or_404(CarType, pk=cartype_no)
    cars = Vehicle.objects.filter(car_type=cartype)
    return render(request, 'primewheelsapp/cardetail.html', {'cartype': cartype, 'cars': cars})

# def cardetail(request, cartype_no):
#     cartype = get_object_or_404(CarType, pk=cartype_no)
#     cars = Vehicle.objects.filter(car_type=cartype)
#     response = HttpResponse()
#     heading = '<p>' + 'Cars of ' + str(cartype) + ':' + '</p>'
#     response.write(heading)
#     for car in cars:
#         para = '<p>' + str(car.id) + ': ' + str(car) + ' - ' + str(int(car.car_price)) + '</p>'
#         response.write(para)
#     return response

def vehicles(request):
    vehicle_list = Vehicle.objects.filter(inventory__gt=0)
    return render(request, 'primewheelsapp/vehicles.html', {'vehicles': vehicle_list})

def orderhere(request):
    return render(request, 'primewheelsapp/order.html')
# def teammembers(request):
#     team_members = LabMember.objects.all().order_by('first_name')
#     response = HttpResponse()
#     heading = '<p>' + 'Team Members:' + '</p>'
#     response.write(heading)
#     for member in team_members:
#         para = '<p>' + str(member.first_name) + ' ' + str(member.last_name) + '</p>'
#         response.write(para)
#     return response

class TeamMembersView(ListView):
    model = LabMember
    template_name = 'primewheelsapp/team.html'  # This should be the path within the templates folder
    context_object_name = 'team_members'

    def get_queryset(self):
        return LabMember.objects.all().order_by('first_name')

