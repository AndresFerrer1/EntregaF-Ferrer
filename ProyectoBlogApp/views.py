from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, request
from ProyectoBlogApp.forms import *
from ProyectoBlogApp.models import EventoSugerido, VideoJuego, Plataforma, Participante, Evento

from asyncio.windows_events import NULL
from cmath import log
from dataclasses import field
import imp
from pyexpat import model
from queue import Empty
import re
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, request
from ProyectoBlogApp.forms import AvatarFormulario, ContactoFormumlario, UserEditForm
from ProyectoBlogApp.models import Avatar, Contact, Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import generic

# Create your views here.

def inicio(req):

    avatar = Avatar.objects.filter(user=req.user.id) 

    try:
        return render(req, 'ProyectoBlogApp/inicio.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/inicio.html', {"url":""})

def bienvenida(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    try:
        return render(req, 'ProyectoBlogApp/bienvenida.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/bienvenida.html', {"url":""})

def agradecimiento(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    try:
        return render(req, 'ProyectoBlogApp/agradecimiento.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/agradecimiento.html', {"url":""})

def eventoformulario(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    if(req.method == 'POST'):

        formulario_evento = EventoFormulario(req.POST)

        if (formulario_evento.is_valid()):

            data = formulario_evento.cleaned_data
        
            evento = EventoSugerido (nombre=data['nombre'], plataforma=data['plataforma'])
            evento.save()

            try:
                return render(req, 'ProyectoBlogApp/agradecimiento.html', {"url":avatar[0].imagen.url})
            except:
                return render(req, 'ProyectoBlogApp/agradecimiento.html', {"url":""})

    else:

        formulario_evento = EventoFormulario()

        try:
            return render(req, 'ProyectoBlogApp/eventoformulario.html', {'form': formulario_evento, "url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/eventoformulario.html', {'form': formulario_evento, "url":""})

def crearparticipante(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    if(req.method == 'POST'):

        formulario_participante = ParticipanteFormulario(req.POST)

        if (formulario_participante.is_valid()):

            data = formulario_participante.cleaned_data
        
            participante = Participante (nombre=data['nombre'], apellido=data['apellido'], email=data['email'], evento=data['evento'])
            participante.save()

            try:
                return render(req, 'ProyectoBlogApp/bienvenida.html', {"url":avatar[0].imagen.url})
            except:
                return render(req, 'ProyectoBlogApp/bienvenida.html', {"url":""})

    else:

        formulario_participante = ParticipanteFormulario()

        try:
            return render(req, 'ProyectoBlogApp/crearparticipante.html', {'form': formulario_participante, "url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/crearparticipante.html', {'form': formulario_participante, "url":""})

def plataforma(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    lista = Plataforma.objects.all()

    try:
        return render(req, 'ProyectoBlogApp/plataforma.html', {"lista": lista, "url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/plataforma.html', {"lista": lista, "url":""})

def evento(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    lista = Evento.objects.all()

    try:
        return render(req, 'ProyectoBlogApp/evento.html', {"lista": lista, "url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/evento.html', {"lista": lista, "url":""})

def eventosugeridos(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    lista = EventoSugerido.objects.all()

    try:
        return render(req, 'ProyectoBlogApp/eventosug_lista.html', {"lista": lista, "url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/eventosug_lista.html', {"lista": lista, "url":""})

def buscarevento(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    try:
        return render(req, 'ProyectoBlogApp/buscarevento.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/buscarevento.html', {"url":""})

def errorformulario(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    try:
        return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":""})

def buscar(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    if(req.method == "GET"):

        nombre = req.GET['nombre']
        plataforma = Evento.objects.filter (nombre=nombre)

        try:
            return render(req, 'ProyectoBlogApp/resultadobusquedaevento.html', {'nombre': nombre, 'plataforma': plataforma, "url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/resultadobusquedaevento.html', {'nombre': nombre, 'plataforma': plataforma, "url":""})

    else:

        try:
            return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":""})

def buscarparticipante(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    try:
        return render(req, 'ProyectoBlogApp/buscarparticipante.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/buscarparticipante.html', {"url":""})

def buscarparticipante2(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    if(req.method == "GET"):

        nombre = req.GET['nombre']
        apellido = Participante.objects.filter (nombre=nombre)

        try:
            return render(req, 'ProyectoBlogApp/resultadobusqparticipante.html', {'nombre': nombre, 'apellido': apellido, "url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/resultadobusqparticipante.html', {'nombre': nombre, 'apellido': apellido, "url":""})

    else:

        try:
            return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":""})

def buscareventosugerido(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    try:
        return render(req, 'ProyectoBlogApp/buscareventosug.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/buscareventosug.html', {"url":""})

def buscareventosug2(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    if(req.method == "GET"):

        nombre = req.GET['nombre']
        plataforma = EventoSugerido.objects.filter (nombre=nombre)

        try:
            return render(req, 'ProyectoBlogApp/resultadobusqeventosug.html', {'nombre': nombre, 'plataforma': plataforma, "url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/resultadobusqeventosug.html', {'nombre': nombre, 'plataforma': plataforma, "url":""})

    else:

        try:
            return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/errorformulario.html', {"url":""})


# Area usuario


def login_request(req):

    if req.method == "POST":
        form = AuthenticationForm(req, data = req.POST)

        if form.is_valid():
            # usuario = form.cleaned_data.get('username')
            # contra = form.cleaned_data.get('password')

            data = form.cleaned_data

            # user = authenticate(username=usuario, password=contra)

            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                login(req, user)

                avatar = Avatar.objects.filter(user=req.user.id)

                try:
                    return render(req, 'ProyectoBlogApp/inicio.html', {'mensaje':f'Bienvenido {user.get_username()}',"url":avatar[0].imagen.url})
                except:
                    return render(req, 'ProyectoBlogApp/inicio.html', {'mensaje':f'Bienvenido {user.get_username()}',"url":""})     


            else:

                return render(req, "ProyectoBlogApp/login.html", {'mensaje':f'Falló la autenticación, intentalo de nuevo', 'form':form})

        else:

            return render(req, "ProyectoBlogApp/login.html", {'mensaje':f'Error, formulario erroneo','form':form})

    form =AuthenticationForm()

    return render(req, "ProyectoBlogApp/login.html", {'form':form})

def register(req):

    if req.method == "POST":

        form = UserCreationForm(req.POST)
        # form2 =AvatarFormulario(req.POST, req.FILES)
        if form.is_valid():

            username = form.cleaned_data['username']
            # imagen = form.cleaned_data['imagen']
            form.save()
            return render(req,"ProyectoBlogApp/inicio.html", {"mensaje":"Usuario Creado, crea un avatar :)"})

    else:

        form = UserCreationForm()
        # form2 =AvatarFormulario()

        return render(req, "ProyectoBlogApp/registro.html", {"form":form})

@login_required
def editarPerfil(req):

    avatar = Avatar.objects.filter(user=req.user.id)  

    usuario = req.user

    if req.method == "POST":
        miFormulario = UserEditForm(req.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            #Si quisiera cambiar el nombre del usuario
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            try:
                return render(req, 'ProyectoBlogApp/inicio.html', {"usuario":usuario,"url":avatar[0].imagen.url})
            except:
                return render(req, 'ProyectoBlogApp/inicio.html', {"usuario":usuario,"url":""})  

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

        try:
            return render(req, 'ProyectoBlogApp/editarPerfil.html', {"miFormulario":miFormulario, "usuario":usuario,"url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/editarPerfil.html', {"miFormulario":miFormulario, "usuario":usuario,"url":""})   


@login_required
def perfil(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    try:
        return render(req, 'ProyectoBlogApp/perfil.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/perfil.html', {"url":""})



# Area Avatar


class AvatarUserList(LoginRequiredMixin, ListView):

    model = Avatar
    template_name = "ProyectoBlogApp/avatar_list.html"

class UpdateAvatar(LoginRequiredMixin, UpdateView):

    model = Avatar
    success_url = "/ProyectoBlogApp/avatarView"
    fields = ['user','imagen']  

class AvatarCreate(CreateView):
    model = Avatar
    fields = ['user', 'imagen']
    success_url = "/ProyectoBlogApp/avatarView"

class AvatarDelete(LoginRequiredMixin, DeleteView):
    model = Avatar
    success_url = "/ProyectoBlogApp/avatarView"
    template_name = "ProyectoBlogApp/avatar_confirm_delete.html"

@login_required
def agregarAvatar(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    if req.method == "POST":
        miFormulario = AvatarFormulario(req.POST, req.FILES)
        if miFormulario.is_valid():

            u = User.objects.get(username=req.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])

            avatar.save()

        try:
            return render(req, 'ProyectoBlogApp/inicio.html', {'mensaje':f'Avatar actualizado',"url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/inicio.html', {'mensaje':f'Avatar actualizado',"url":""})

            # return render(req, 'AppCoder/inicio.html', {'mensaje':f'Avatar actualizado'})

    else:

        miFormulario = AvatarFormulario()

        try:
            return render(req, 'ProyectoBlogApp/agregarAvatar.html', {'miFormulario':miFormulario, "url":avatar[0].imagen.url})
        except:
            return render(req, 'ProyectoBlogApp/agregarAvatar.html', {'miFormulario':miFormulario,"url":""})

    # return render(req, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})

# def indice(req):

#     return render(req, 'AppCoder/indice.html',{})


# Area Contacto

class crearContacto(CreateView):
    model = Contact
    fields = ['correo', 'nombre', 'apellido', 'asunto', 'mensaje']
    success_url = "/ProyectoBlogApp/contacto_gracias"

def contacto_gracias(req):

    avatar = Avatar.objects.filter(user=req.user.id)

    mensaje1 = f'Gracias por enviarnos tu consulta. Nos pondremos en contacto a la brevedad'

    try:
        return render(req, 'ProyectoBlogApp/contacto_gracias.html', {'mensaje1':mensaje1,"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/contacto_gracias.html', {'mensaje1':mensaje1,"url":""})




# Area Post

class VistaPost(ListView):
    model = Post
    template_name = 'ProyectoBlogApp/listaPost.html'
    ordering = ['fecha_post']
    context_object_name = 'post'  # Default: object_list
    paginate_by = 2
    queryset = Post.objects.all()  # Default: Model.objects.all()

class DetallePost(DetailView):
    model = Post
    template_name = 'ProyectoBlogApp/detallePost.html'

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'etiqueta_titulo', 'autor', 'body', 'imagen']
    success_url = "/ProyectoBlogApp/listaPost"

class ActualizarPost(LoginRequiredMixin, UpdateView):

    model = Post
    success_url = "/ProyectoBlogApp/listaPost"
    fields = ['titulo', 'etiqueta_titulo', 'body', 'imagen']

class BorrarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/ProyectoBlogApp/listaPost"
    template_name = "ProyectoBlogApp/post_confirm_delete.html"


# Area acerca de mi

def aboutMe(req):

    avatar = Avatar.objects.filter(user=req.user.id) 

    try:
        return render(req, 'ProyectoBlogApp/aboutMe.html', {"url":avatar[0].imagen.url})
    except:
        return render(req, 'ProyectoBlogApp/aboutMe.html', {"url":""})