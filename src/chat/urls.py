from django.urls import path
from chat.views import *

urlpatterns = [
    path('', MensajeList.as_view(), name='chat'),
    path('enviar/', enviar_mensaje, name='enviar_mensaje')
]
