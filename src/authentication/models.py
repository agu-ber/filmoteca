from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your models here.

class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    