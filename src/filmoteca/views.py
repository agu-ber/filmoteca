from django.shortcuts import render
from django.http import HttpResponse
from filmoteca.models import *

# Create your views here.

def index(request):

    return render(request, 'filmoteca/index.html')

def peliculas(request):

    lista_peliculas = Pelicula.objects.all()

    return render(request, 'filmoteca/peliculas.html', {"peliculas": lista_peliculas})

def directores(request):

    lista_directores = Director.objects.all()

    return render(request, 'filmoteca/directores.html', {"directores": lista_directores})

def actores(request):

    lista_actores = Actor.objects.all()

    return render(request, 'filmoteca/actores.html', {"actores": lista_actores})
    