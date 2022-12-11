from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *
from .forms import *

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class SignupView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy("Inicio")
    template_name = "AppUser/Templates/AppUser/registro.html"

class AdminLoginView(LoginView):

    template_name = "AppUser/Templates/AppUser/login.html"

class AdminLogoutView(LoginRequiredMixin, LogoutView):

    template_name = "AppUser/Templates/AppUser/logout.html"

def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.username = informacion["username"]
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]

            usuario.save()

            return render(request, "AppWeb/Templates/AppWeb/index.html")

    else:
        formulario = UserEditForm(initial={
            "username": usuario.username,
            "email": usuario.email,
            })

    return render(request, "AppUser/Templates/AppUser/admin_update.html", {
        "form": formulario,
        "usuario": usuario
        })

@login_required
def add_avatar(request):

    if request.method == 'POST':

        miAvatar = Avatar_form(request.POST, request.FILES)

        if miAvatar.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            file = miAvatar.cleaned_data

            if len(avatar) > 0:

                avatar = avatar[0]
                avatar.imagen = file['img']
                avatar.save()

                avatar = Avatar.objects.filter(user=request.user)

                img = avatar[0].imagen.url

            else:

                avatar = Avatar(user=usuario, imagen=miAvatar.cleaned_data['img'])
                avatar.save()

                img = None

        return render(request, 'AppWeb/Templates/AppWeb/index.html', {'img':img})

    else:

        miAvatar = Avatar_form()

        img = None
        
        return render(request, 'AppUser/Templates/AppUser/addavatar.html', {'miAvatar': miAvatar, 'img': img})