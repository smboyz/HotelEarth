from django.contrib import admin
from django.urls import path
from .views import *
from .views import admin_login, dashboard, Logoutpage



urlpatterns = [
    path("", admin_login, name="admin_login"),
    path("dashboard/",dashboard, name="dashboard"),
    path("logout/", Logoutpage, name="logout"),
    path("globalsetting/", globalsetting, name="globalsetting"),
    path("main_navigation/", main_navigation, name="main_navigation"),
    path("main_navigation/<int:parent_id>/", main_navigation, name="main_navigation"),
    path("navigation/", navigation, name="navigation"),
    path("navigation/<int:parent_id>/", navigation, name="navigation"),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="delete"),  
    path("contact_us",contact_us,name="contact_us"),
    path("delete_contact_us/<int:pk>/", delete_contact_us, name="delete_contact_us"), 
    path('gallery',gallery,name='gallery'),
    path('gallery_create',gallery_create,name='gallery_create'),
    path('gallery_update/<int:pk>/',gallery_update,name='gallery_update'),
    path('gallery_delete/<int:pk>/',gallery_delete,name="gallery_delete"),
    path('slider/',slider,name='slider'),
    path('slider_create/',slider_create,name='slider_create'),
    path('slider_update/<int:pk>/',slider_update,name='slider_update'),
    path('slider_delete//<int:pk>/',slider_delete,name='slider_delete'),
    path('room_detals/',room_details,name='room_details'),
    path('room_create/',room_create,name='room_create'),
    path('room_update/<int:pk>/',room_update,name='room_update'),
    path('room_delete/<int:pk>/',room_delete,name='room_delete'),
    path('review_detals/',review_details,name='review_details'),
    path('review_create/',review_create,name='review_create'),
    path('review_update/<int:pk>/',review_update,name='review_update'),
    path('review_delete/<int:pk>/',review_delete,name='review_delete'),
    path('hotel_component/',hotel_component,name='hotel_component'),
    path('hotel_component_update/<int:pk>/',hotel_component_update,name='hotel_component_update'),
    path('hotel_component_delete/<int:pk>/',hotel_component_delete,name='hotel_component_delete'),
    path('check',check,name='check'),
    path('key_features/',key_features,name='key_features'),
    path('key_features/<int:parent_id>/',key_features,name='key_features'),
    path('create_features/',create_features,name='create_features'),
    path('create_features/<int:parent_id>/',create_features,name='create_features'),
    path('update_features/<int:pk>/',update_features,name='update_features'),
    path('delete_features/<int:pk>/',delete_features,name='delete_features'),
    
]