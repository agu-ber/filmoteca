from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request, 'filmoteca/index.html')

def peliculas(request):

    return HttpResponse('Vista de películas')

def directores(request):

    return HttpResponse('Vista de directores')

def actores(request):

    return HttpResponse('Vista de actores')