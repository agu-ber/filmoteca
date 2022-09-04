from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from filmoteca.forms import UserRegisterForm

# Create your views here.

def user_login(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {"form": form})

    else:
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                return redirect("index")

            else:
                context = {
                    "error": "Credenciales no válidas",
                    "form": form
                }
                return render(request, "authentication/login.html", context)

        else:
            context = {
                "form": form,
                "error": "Formulario no válido",
            }
            return render(request, "authentication/login.html", context)


def user_register(request):

    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, "authentication/register.html", {"form": form})

    else:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

        else:
            context = {
                "form": form,
                "error": "Formulario no válido"
            }
            return render(request, "authentication/register.html", context)