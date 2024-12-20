from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('tracking-shipment/', views.tracking, name="tracking"),

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
