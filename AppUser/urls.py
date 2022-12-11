from AppUser import views
from django.urls import path
from AppUser.views import *

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="Sign Up"),
    path("login/", views.AdminLoginView.as_view(), name="Login"),
    path("logout/", views.AdminLogoutView.as_view(), name="Logout"),
    path("edit/", views.editar_usuario, name="Edit"),
    path("accounts/addavatar/", add_avatar, name='addAvatar'),
]