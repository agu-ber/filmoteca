from csv import Dialect
from django.contrib import admin
from filmoteca.models import *

# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Actor)