from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from filmoteca.models import *
from filmoteca.forms import *

# Create your views here.

def index(request):

    return render(request, 'filmoteca/index.html')


class PeliculaList(ListView):

    model = Pelicula
    template_name = "filmoteca/pelicula_list.html"


class PeliculaDetail(DetailView):
    
    model = Pelicula
    template_name = "filmoteca/pelicula_detail.html"


class PeliculaCreate(LoginRequiredMixin, CreateView):

    model = Pelicula
    success_url = "/peliculas"
    fields = ['titulo', 'director', 'genero', 'duracion', 'estreno', 'poster']


class PeliculaUpdate(LoginRequiredMixin, UpdateView):

    model = Pelicula
    success_url = "/peliculas"
    fields = ['titulo', 'director', 'genero', 'duracion', 'estreno', 'poster']


class PeliculaDelete(LoginRequiredMixin, DeleteView):

    model = Pelicula
    success_url = "/peliculas"


def peliculas_resultados(request):

    if request.GET["titulo"]:

        busqueda = request.GET["titulo"]
        peliculas = Pelicula.objects.filter(titulo__icontains=busqueda)

        return render(request, 'filmoteca/peliculas_resultados.html', {"busqueda": busqueda, "peliculas": peliculas})

    else:

        return render(request, 'filmoteca/peliculas.html')

class DirectorList(ListView):

    model = Director
    template_name = "filmoteca/director_list.html"


class DirectorDetail(DetailView):
    
    model = Director
    template_name = "filmoteca/director_detail.html"


class DirectorCreate(LoginRequiredMixin, CreateView):

    model = Director
    success_url = "/directores"
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'cant_peliculas', 'esta_activo', 'foto']


class DirectorUpdate(LoginRequiredMixin, UpdateView):

    model = Director
    success_url = "/directores"
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'cant_peliculas', 'esta_activo', 'foto']


class DirectorDelete(LoginRequiredMixin, DeleteView):

    model = Director
    success_url = "/directores"


def directores_resultados(request):
    
    if request.GET["apellido"]:

        busqueda = request.GET["apellido"]
        directores = Director.objects.filter(apellido__icontains=busqueda)

        return render(request, 'filmoteca/directores_resultados.html', {"busqueda": busqueda, "directores": directores})

    else:

        return render(request, 'filmoteca/directores.html')


class ActorList(ListView):

    model = Actor
    template_name = "filmoteca/actor_list.html"


class ActorDetail(DetailView):
    
    model = Actor
    template_name = "filmoteca/actor_detail.html"


class ActorCreate(LoginRequiredMixin, CreateView):

    model = Actor
    success_url = "/actores"
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'pelicula_debut', 'esta_activo', 'foto']


class ActorUpdate(LoginRequiredMixin, UpdateView):

    model = Actor
    success_url = "/actores"
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'pelicula_debut', 'esta_activo', 'foto']


class ActorDelete(LoginRequiredMixin, DeleteView):

    model = Actor
    success_url = "/actores"


def actores_resultados(request):

    if request.GET["apellido"]:

        busqueda = request.GET["apellido"]
        actores = Actor.objects.filter(apellido__icontains=busqueda)

        return render(request, 'filmoteca/actores_resultados.html', {"busqueda": busqueda, "actores": actores})

    else:

        return render(request, 'filmoteca/actores.html')
