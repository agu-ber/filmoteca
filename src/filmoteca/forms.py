from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    esta_activo = forms.BooleanField(required=False)


class ActorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20) 
    apellido = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField()
    pelicula_debut = forms.CharField(max_length=60)
    esta_activo = forms.BooleanField(required=False)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}
