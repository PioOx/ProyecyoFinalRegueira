from AppWeb. views import *
from AppWeb import views
from django.urls import path

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('crear_noticia/', NoticiaCreateView.as_view(), name="CrearNoticia"),
    path("lista_noticia/", views.NoticiaListView.as_view(), name="lista"),
    path("detail_noticia/<pk>", views.NoticiaDetailView.as_view(), name="detail"),
    path("noticiamodels_confirm_delete/<pk>", views.NoticiaDeleteView.as_view(), name="delete"),
    path("noticiamodels_form/<pk>", views.NoticiaUpdateView.as_view(), name="update"),
]