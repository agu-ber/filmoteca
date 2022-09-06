from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView
from authentication.views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name="authentication/logout.html"), name='logout'),
    path('register/', user_register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit', user_edit, name='edit_user'),
    path('avatar/eliminar/<pk>', DeleteAvatar.as_view(), name='delete_avatar'),
    path('avatar/', add_avatar, name='add_avatar'),
    path('password/', PasswordChangeView.as_view(template_name="authentication/change_password.html", success_url="/profile"), name='change_password')
]
