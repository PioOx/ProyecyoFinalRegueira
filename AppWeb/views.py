from django.shortcuts import render
from .models import *
from .forms import *
from AppUser.models import Avatar
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.db.models import Q

def inicio(request):
    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        usuario = request.user

        if len(avatar) > 0:

            img = avatar[0].imagen.url

        else:

            img = None

    else:

        img = None

        usuario = None

    return render(request, "AppWeb\Templates\AppWeb\index.html", {'user': usuario, 'img':img})

def busqueda(request):
    if request.GET.get("Titulo", False):
        Titulo = request.GET ["Titulo"]
        noticias = NoticiaModel.objects.filter(Titulo__icontains=Titulo)

        return render(request, "AppWeb/Templates/AppWeb/buscador.html", {"noticias":noticias})

    else:
        Mensaje = "No existen noticias aun..."
    return render(request, "AppWeb/Templates/AppWeb/buscador.html", {"respuesta":Mensaje})

@login_required
def noticia_funcion(request):
    mensaje = None
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = "Posteo cargado con exito, te invito a ver todos "
    else:
        form = NoticiaForm()

    return render(request, "AppWeb/Templates/AppWeb/crear_noticia_funcion.html", {"form":form, "mensaje":mensaje})

class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = NoticiaModel
    form = NoticiaForm
    fields = "__all__"
    success_url = "/lista_noticia"

class NoticiaListView(ListView):
    model = NoticiaModel
    template = "AppWeb/Templates/AppWeb/noticiamodel_list.html"

class NoticiaDetailView(DetailView):
    model = NoticiaModel
    template= "AppWeb/noticiamodel_detail.html"

class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model = NoticiaModel
    success_url = "/lista_noticia"

class NoticiaUpdateView(LoginRequiredMixin, UpdateView):

    model = NoticiaModel
    form = NoticiaForm
    fields = "__all__"
    success_url = "/lista_noticia"