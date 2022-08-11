from django.shortcuts import render
from django.http import HttpResponse
from filmoteca.models import *
from filmoteca.forms import *

# Create your views here.

def index(request):

    return render(request, 'filmoteca/index.html')

def peliculas(request):

    lista_peliculas = Pelicula.objects.all()

    return render(request, 'filmoteca/peliculas.html', {"peliculas": lista_peliculas})

def peliculas_añadir(request):

    if request.method == 'GET':
         formulario = PeliculaFormulario()

    else:
        formulario = PeliculaFormulario(request.POST)

        if formulario.is_valid():
            datos_limpios = formulario.cleaned_data

            pelicula = Pelicula(titulo=datos_limpios['titulo'], director=datos_limpios['director'], genero=datos_limpios['genero'], duracion=datos_limpios['duracion'], estreno=datos_limpios['estreno'])
            pelicula.save()

            return render(request, 'filmoteca/index.html')

    return render(request, 'filmoteca/peliculas_añadir.html', {"formulario": formulario})

def peliculas_resultados(request):

    if request.GET["titulo"]:

        busqueda = request.GET["titulo"]
        peliculas = Pelicula.objects.filter(titulo__icontains=busqueda)

        return render(request, 'filmoteca/peliculas_resultados.html', {"busqueda": busqueda, "peliculas": peliculas})

    else:

        return render(request, 'filmoteca/peliculas.html')

def directores(request):

    lista_directores = Director.objects.all()

    return render(request, 'filmoteca/directores.html', {"directores": lista_directores})

def directores_añadir(request):

    if request.method == 'GET':
         formulario = DirectorFormulario()

    else:
        formulario = DirectorFormulario(request.POST)

        if formulario.is_valid():
            datos_limpios = formulario.cleaned_data

            director = Director(nombre=datos_limpios['nombre'], apellido=datos_limpios['apellido'], fecha_nacimiento=datos_limpios['fecha_nacimiento'], cant_peliculas=datos_limpios['cant_peliculas'], esta_activo=datos_limpios['esta_activo'])
            director.save()

            return render(request, 'filmoteca/index.html')

    return render(request, 'filmoteca/directores_añadir.html', {"formulario": formulario})

def directores_resultados(request):
    
    if request.GET["apellido"]:

        busqueda = request.GET["apellido"]
        directores = Director.objects.filter(apellido__icontains=busqueda)

        return render(request, 'filmoteca/directores_resultados.html', {"busqueda": busqueda, "directores": directores})

    else:

        return render(request, 'filmoteca/directores.html')

def actores(request):

    lista_actores = Actor.objects.all()

    return render(request, 'filmoteca/actores.html', {"actores": lista_actores})

def actores_añadir(request):

    if request.method == 'GET':
         formulario = ActorFormulario()

    else:
        formulario = ActorFormulario(request.POST)

        if formulario.is_valid():
            datos_limpios = formulario.cleaned_data

            actor = Actor(nombre=datos_limpios['nombre'], apellido=datos_limpios['apellido'], fecha_nacimiento=datos_limpios['fecha_nacimiento'], pelicula_debut=datos_limpios['pelicula_debut'], esta_activo=datos_limpios['esta_activo'])
            actor.save()

            return render(request, 'filmoteca/index.html')

    return render(request, 'filmoteca/actores_añadir.html', {"formulario": formulario})

def actores_resultados(request):

    if request.GET["apellido"]:

        busqueda = request.GET["apellido"]
        actores = Actor.objects.filter(apellido__icontains=busqueda)

        return render(request, 'filmoteca/actores_resultados.html', {"busqueda": busqueda, "actores": actores})

    else:

        return render(request, 'filmoteca/actores.html')
