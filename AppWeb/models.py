from django.db import models
from django.contrib.auth.models import User

class NoticiaModel(models.Model):

    Autor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=40)
    Noticia = models.TextField(max_length=10**10, null=True, blank=True)
    Imagen = models.ImageField(upload_to="media", null=False, blank=True)

    def __str__(self) -> str:
        return f'{self.Titulo} | {self.Autor}'