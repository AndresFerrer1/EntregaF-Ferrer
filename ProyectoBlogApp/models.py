from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class VideoJuego(models.Model):
    nombre = models.CharField(max_length=80)
    plataforma = models.CharField(max_length=80)

    def __str__(self):
        return (f'{self.nombre}-{self.plataforma}')

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return (f'{self.nombre}')

class Participante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    evento = models.CharField(max_length=30)

    def __str__(self):
        return (f'{self.nombre} {self.apellido} - {self.email} - Evento: {self.evento}')

class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    nro_evento = models.IntegerField()
    plataforma = models.CharField(max_length=80)
    fechaDeInicio = models.DateField()
    
    def __str__(self):
        return (f'{self.nombre} - Evento Nro: {self.nro_evento}  - {self.plataforma}')

class EventoSugerido(models.Model):
    nombre = models.CharField(max_length=30)
    plataforma = models.CharField(max_length=80)

    def __str__(self):
        return (f'{self.nombre} - {self.plataforma}')

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de {self.user.username}"

class Contact(models.Model):
    correo = models.EmailField()
    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField(max_length=10000)

    def __str__(self):
        return self.correo

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    etiqueta_titulo = models.CharField(max_length=255, default="Etiqueta del Post")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    fecha_post = models.DateField(auto_now_add=True)
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)