from django.urls import path 
from primewheelsapp import views
app_name = 'primewheelsapp'
urlpatterns = [ 
    path('', views.homepage, name='homepage'), 
    path('aboutus/', views.aboutus, name='aboutus'),
    path('<int:cartype_no>/', views.cardetail, name='cardetail'),
    path('team/', views.teammembers, name='teammembers'),
    ]
