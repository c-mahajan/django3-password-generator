from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    return render(request, "generator/index.html")

def password(request):
    thepassword=""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.POST.get("Uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.POST.get('numbers'):
        characters.extend(list('1234567890'))

    if request.POST.get('Symbols'):
        characters.extend(list('!@#$%&_'))

    length=int(request.POST["length"])
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html",{
        "password":thepassword,
    })
