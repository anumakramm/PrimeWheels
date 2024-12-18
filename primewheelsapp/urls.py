from django.urls import path
from primewheelsapp import views

app_name = 'primewheelsapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('<int:cartype_no>/', views.cardetail, name='cardetail'),
    path('team/', views.TeamMembersView.as_view(), name='teammembers'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('orderhere', views.orderhere, name='orderhere'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.login_here, name='login_here'),
    path('logout/', views.logout_here, name='logout'),
]