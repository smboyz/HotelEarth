from django.contrib import admin
from django.urls import path
from hotel import views



urlpatterns = [
    path("", views.Base, name="home"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("contact/", views.contact, name="contact"),
    path("features/", views.features, name="features"),
    path("services/", views.services, name="services"),
    path("rooms/", views.rooms, name="rooms"),
    
    

]
