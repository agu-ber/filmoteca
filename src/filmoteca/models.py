from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=60)
    director = models.CharField(max_length=40)
    genero = models.CharField(max_length=20)
    duracion = models.IntegerField()
    estreno = models.IntegerField()
    poster = models.ImageField(upload_to="posters")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titulo}"

class Director(models.Model):
    nombre = models.CharField(max_length=20) 
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    cant_peliculas = models.IntegerField()
    esta_activo = models.BooleanField()
    foto = models.ImageField(upload_to="fotos_directores")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Actor(models.Model):
    nombre = models.CharField(max_length=20) 
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    pelicula_debut = models.CharField(max_length=60)
    esta_activo = models.BooleanField()
    foto = models.ImageField(upload_to="fotos_actores")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        