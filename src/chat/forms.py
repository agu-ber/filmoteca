from socket import fromshare
from django import forms

class MensajeForm(forms.Form):
    mensaje = forms.CharField(max_length=100)