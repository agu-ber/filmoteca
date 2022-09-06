from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from authentication.forms import *
from authentication.models import *

# Create your views here.


def user_login(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {"form": form})

    else:
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = authenticate(username=data.get(
                "username"), password=data.get("password"))

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


@login_required
def user_edit(request):

    if request.method == "GET":
        form = UserEditForm(initial={"first_name": request.user.first_name,
                            "last_name": request.user.last_name, "email": request.user.email})

        return render(request, "authentication/edit_user.html", {"form": form})

    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = request.user

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()

            return redirect("index")

        else:
            context = {
                "form": form,
                "error": "Formulario no válido"
            }

            return render(request, "authentication/edit_user.html", context)


@login_required
def add_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        return render(request, "authentication/add_avatar.html", {"form": form})

    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            usuario = User.objects.filter(username=request.user.username).first()
            avatar = Avatar(usuario=usuario, avatar=data["avatar"])

            avatar.save()

            return redirect("index")

        else:
            context = {
                "form": form,
                "error": "Formulario no válido"
            }

            return render(request, "authentication/add_avatar.html", context)
