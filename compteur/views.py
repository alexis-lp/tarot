from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import *
from .models import *


# Create your views here.

def accueil(request):
    return render(request,'compteur/home.html')

def newgame(request):
    error = False
    form = newGameForm(request.POST or None)

    if form.is_valid():
        tarot_game = form.save()
        return redirect(reverse('accueil de la partie', args=[tarot_game.id]))

    return render(request,'compteur/newgame.html',locals())

def game(request,game_id):
    return render(request,'compteur/game.html', locals())
