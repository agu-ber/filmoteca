from django.urls import path
from filmoteca.views import *

urlpatterns = [
    path('', index, name='index'),
    path('peliculas/', peliculas, name='peliculas'),
    path('peliculas/añadir/', peliculas_añadir, name='peliculas_añadir'),
    path('peliculas/resultados', peliculas_resultados, name='peliculas_resultados'),
    path('directores/', directores, name='directores'),
    path('directores/añadir/', directores_añadir, name='directores_añadir'),
    path('directores/resultados', directores_resultados, name='directores_resultados'),
    path('actores/', actores, name='actores'),
    path('actores/añadir/', actores_añadir, name='actores_añadir'),
    path('actores/resultados', actores_resultados, name='actores_resultados'),
]
