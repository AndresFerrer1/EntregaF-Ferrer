from django.contrib import admin

from ProyectoBlogApp.models import * #importamos todo los models

# Register your models here.
# Registramos los modelos

admin.site.register(VideoJuego)

admin.site.register(Participante)

admin.site.register(Plataforma)

admin.site.register(Evento)

admin.site.register(EventoSugerido)

admin.site.register(Avatar)

admin.site.register(Contact)

admin.site.register(Post)