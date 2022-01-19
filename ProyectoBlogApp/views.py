from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, request
from ProyectoBlogApp.forms import *
from ProyectoBlogApp.models import EventoSugerido, VideoJuego, Plataforma, Participante, Evento

# Create your views here.

def inicio(req):

    return render(req, 'ProyectoBlogApp/inicio.html')

def bienvenida(req):

    return render(req, 'ProyectoBlogApp/bienvenida.html')

def agradecimiento(req):

    return render(req, 'ProyectoBlogApp/agradecimiento.html')

# def crea_videojuego(req, nombre, plataforma):

#     juego = VideoJuego(nombre=nombre, plataforma=plataforma)
    
#     juego.save()

#     return HttpResponse(f'Se creo el videojuego {juego.nombre} en la plataforma {juego.plataforma}')

def eventoformulario(req):

    if(req.method == 'POST'):

        formulario_evento = EventoFormulario(req.POST)

        if (formulario_evento.is_valid()):

            data = formulario_evento.cleaned_data
        
            evento = EventoSugerido (nombre=data['nombre'], plataforma=data['plataforma'])
            evento.save()

            return render(req, 'ProyectoBlogApp/agradecimiento.html')

    else:

        formulario_evento = EventoFormulario()

    return render(req, 'ProyectoBlogApp/eventoformulario.html', {'form': formulario_evento})

def crearparticipante(req):

    if(req.method == 'POST'):

        formulario_participante = ParticipanteFormulario(req.POST)

        if (formulario_participante.is_valid()):

            data = formulario_participante.cleaned_data
        
            participante = Participante (nombre=data['nombre'], apellido=data['apellido'], email=data['email'], evento=data['evento'])
            participante.save()

            return render(req, 'ProyectoBlogApp/bienvenida.html')

    else:

        formulario_participante = ParticipanteFormulario()

    return render(req, 'ProyectoBlogApp/crearparticipante.html', {'form': formulario_participante})

def plataforma(req):

    lista = Plataforma.objects.all()

    return render(req, 'ProyectoBlogApp/plataforma.html', {"lista": lista})

def evento(req):

    lista = Evento.objects.all()

    return render(req, 'ProyectoBlogApp/evento.html', {"lista": lista})

def buscarevento(req):

    return render(req, 'ProyectoBlogApp/buscarevento.html')

def errorformulario(req):

    return render(req, 'ProyectoBlogApp/errorformulario.html')

def buscar(req):

    if(req.method == "GET"):

        nro_evento = req.GET['nombre']
        nombre = Evento.objects.filter (nro_evento=nro_evento)

        return render(req, "ProyectoBlogApp/resultadobusquedaevento.html", {'nombre': nombre, 'nro_evento': nro_evento})

    else:

        return render(req, 'ProyectoBlogApp/errorformulario.html')

        # return render(HttpResponse(f'No enviaste datos'))

        # return HttpResponse(f'No enviaste datos')
