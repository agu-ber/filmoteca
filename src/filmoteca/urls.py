from django.urls import path
from filmoteca.views import *

urlpatterns = [
    path('', index, name='index'),
    path('peliculas/', peliculas, name='peliculas'),
    path('peliculas/añadir/', peliculas_añadir, name='peliculas_añadir'),
    path('directores/', directores, name='directores'),
    path('directores/añadir/', directores_añadir, name='directores_añadir'),
    path('actores/', actores, name='actores'),
    path('actores/añadir/', actores_añadir, name='actores_añadir'),
]
