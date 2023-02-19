from django.shortcuts import render

# Create your views here.
def LobbyView(request):
    return render(request,'app/lobby.html')

def RoomView(request):
    return render(request,'app/room.html')