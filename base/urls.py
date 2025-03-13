from django.urls import path
from . import views


urlpatterns = [
    path('loginPage/', views.loginPage, name='login'),
    path('RegisterPage/', views.RegisterPage, name='register'),
    path('Logout/', views.LogoutUser, name='logout'),
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('createRoom/', views.createRoom, name='create-room'),
    path('updatedRoom/<str:pk>', views.updatedRoom, name='updated-room'),
    path('deleteRoom/<str:pk>', views.deleteRoom, name='delete-room')
]
