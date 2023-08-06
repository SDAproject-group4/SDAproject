from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('repair/<str:pk>/', views.repair, name='repair'),
    path('create-repair/', views.createRepair, name='createrepair'),
    path('update-repair/<str:pk>/', views.updateRepair, name='updaterepair'),
    path('profile/<str:pk>/', views.userProfile, name='userprofile'),
    path('profile/<str:pk>/', views.userProfile, name='userprofile'),
    
    

]