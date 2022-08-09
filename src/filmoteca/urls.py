from importlib.resources import path
from django.urls import path
from filmoteca.views import *

urlpatterns = [
    path('', index, name='index'),
    path('peliculas/', peliculas, name='peliculas'),
    path('directores/', directores, name='directores'),
    path('actores/', actores, name='actores'),
]
