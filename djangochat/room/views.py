from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

#This function returns a rendered HTML template with a list of all rooms.
@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

#This function retrieves a specific room object and its associated messages and renders them in a template.
@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})