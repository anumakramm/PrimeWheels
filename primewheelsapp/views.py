from django.http import HttpResponse
from .models import CarType, Vehicle, LabMember
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from django.urls import path
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    return render(request, 'primewheelsapp/homepage.html', {'cartype_list': cartype_list})

def aboutus(request):
    return render(request, 'primewheelsapp/aboutus.html')

def cardetail(request, cartype_no):
    cartype = get_object_or_404(CarType, pk=cartype_no)
    cars = Vehicle.objects.filter(car_type=cartype)
    return render(request, 'primewheelsapp/cardetail.html', {'cartype': cartype, 'cars': cars})

def vehicles(request):
    vehicle_list = Vehicle.objects.filter(inventory__gt=0)
    return render(request, 'primewheelsapp/vehicles.html', {'vehicles': vehicle_list})

def orderhere(request):
    return render(request, 'primewheelsapp/order.html')

class TeamMembersView(ListView):
    model = LabMember
    template_name = 'primewheelsapp/team.html'
    context_object_name = 'team_members'

    def get_queryset(self):
        return LabMember.objects.all().order_by('first_name')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'primewheelsapp/signup.html'
    success_url = reverse_lazy('login')

def login_here(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('primewheelsapp:homepage'))
            else:
                return HttpResponse('Your account is disabled')
        else:
            return HttpResponse('Login details are incorrect')
    else:
        return render(request, 'primewheelsapp/login_here.html')

@login_required
def logout_here(request):
    logout(request)
    return HttpResponseRedirect(reverse('primewheelsapp:homepage'))