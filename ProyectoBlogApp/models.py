from django.db import models

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