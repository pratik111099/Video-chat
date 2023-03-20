from django.urls import path
from . import views

urlpatterns = [
    path('', views.LobbyView),
    path('room/', views.RoomView),
    path('get_token/', views.getToken),

    path('create_member/', views.createMemberView),
    path('get_member/', views.getMemberView),
    path('delete_member/', views.deleteMemberView),
]