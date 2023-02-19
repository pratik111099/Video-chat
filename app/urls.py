from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.LobbyView),
    path('room/', views.RoomView),
]