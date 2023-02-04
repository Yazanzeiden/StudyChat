from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name': 'lets learn python!'},
    {'id':2, 'name': 'Desgin with me'},
    {'id':3, 'name': 'frontend developers'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(reuqest, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}        

    return render(reuqest, 'base/room.html', context)