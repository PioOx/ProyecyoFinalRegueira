from django.shortcuts import render
from .models import *
from .forms import *
from AppUser.models import Avatar

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def inicio(request):
    imagenes = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppWeb\Templates\AppWeb\index.html", {"url":imagenes[0].imagen.url})

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