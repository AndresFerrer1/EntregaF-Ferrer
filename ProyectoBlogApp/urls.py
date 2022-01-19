from django.urls import path

from ProyectoBlogApp import views

from ProyectoBlogApp.views import VideoJuego

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    # path('crea_videojuego/', views.crea_videojuego, name="Crear Videojuego"),
    path('eventoformulario/', views.eventoformulario, name="eventoformulario"),
    # path('videojuegos/', views.cursos, name="Cursos"),
    path('plataforma/', views.plataforma, name="plataforma"),
    path('crearparticipante/', views.crearparticipante, name="crearparticipante"),
    path('bienvenida/', views.bienvenida, name="bienvenida"),
    path('evento/', views.evento, name="evento"),
    path('buscarevento/', views.buscarevento, name="buscarevento"),
    path('buscar/', views.buscar, name="buscar"),
    path('errorformulario/', views.errorformulario, name="errorformulario"),
    path('agradecimiento/', views.agradecimiento, name="agradecimiento"),
]