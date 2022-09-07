from django.urls import path
from filmoteca.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),

    path('peliculas/', PeliculaList.as_view(), name='peliculas'),
    path('peliculas/añadir/', PeliculaCreate.as_view(), name='peliculas_añadir'),
    path('peliculas/resultados', peliculas_resultados, name='peliculas_resultados'),
    path('peliculas/editar/<pk>', PeliculaUpdate.as_view(), name='peliculas_editar'),
    path('peliculas/eliminar/<pk>', PeliculaDelete.as_view(), name='peliculas_eliminar'),
    path('peliculas/<pk>', PeliculaDetail.as_view(), name='peliculas_detail'),

    path('directores/', DirectorList.as_view(), name='directores'),
    path('directores/añadir/', DirectorCreate.as_view(), name='directores_añadir'),
    path('directores/resultados', directores_resultados, name='directores_resultados'),
    path('directores/editar/<pk>', DirectorUpdate.as_view(), name='directores_editar'),
    path('directores/eliminar/<pk>', DirectorDelete.as_view(), name='directores_eliminar'),
    path('directores/<pk>', DirectorDetail.as_view(), name='directores_detail'),

    path('actores/', ActorList.as_view(), name='actores'),
    path('actores/añadir/', ActorCreate.as_view(), name='actores_añadir'),
    path('actores/resultados', actores_resultados, name='actores_resultados'),
    path('actores/editar/<pk>', ActorUpdate.as_view(), name='actores_editar'),
    path('actores/eliminar/<pk>', ActorDelete.as_view(), name='actores_eliminar'),
    path('actores/<pk>', ActorDetail.as_view(), name='actores_detail'),
]
