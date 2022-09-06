from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from chat.models import *
from chat.forms import *

# Create your views here.

class MensajeList(LoginRequiredMixin, ListView):

    model = Mensaje
    template_name = "chat/mensaje_list.html"


@login_required
def enviar_mensaje(request):

    if request.method == "GET":
        form = MensajeForm()
        return render(request, "chat/enviar_mensaje.html", {"form": form})

    else:
        form = MensajeForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = User.objects.filter(username=request.user.username).first()
            texto = data["mensaje"]

            mensaje = Mensaje(usuario=usuario, mensaje=texto)

            mensaje.save()

            return redirect("chat")

        else:
            context = {
                "form": form,
                "error": "Formulario no válido"
            }

            return render(request, "chat/enviar_mensaje.html", context)
            