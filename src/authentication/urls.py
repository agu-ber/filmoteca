from django.urls import path
from django.contrib.auth.views import LogoutView
from authentication.views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name="authentication/logout.html"), name='logout'),
    path('register/', user_register, name='register'),
]
