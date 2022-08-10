from django import forms

class PeliculaFormulario(forms.Form):
    titulo = forms.CharField(max_length=60)
    director = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=20)
    duracion = forms.IntegerField()
    estreno = forms.IntegerField()

class DirectorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20) 
    apellido = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField()
    cant_peliculas = forms.IntegerField()
    esta_activo = forms.BooleanField()

class ActorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20) 
    apellido = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField()
    pelicula_debut = forms.CharField(max_length=60)
    esta_activo = forms.BooleanField()
