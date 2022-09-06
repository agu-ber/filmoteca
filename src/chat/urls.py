from django.urls import path
from chat.views import *

urlpatterns = [
    path('chat/', MensajeList.as_view(), name='chat'),
    path('chat/enviar', enviar_mensaje, name='enviar_mensaje')
]
