from dataclasses import fields
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ProyectoBlogApp.models import Avatar, Post


class EventoFormulario(forms.Form):
    nombre = forms.CharField()
    plataforma = forms.CharField(max_length=80)

class PlataformaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)

class ParticipanteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    evento = forms.CharField(max_length=30)

class Evento(forms.Form):
    nombre = forms.CharField(max_length=30)
    nro_evento = forms.IntegerField()
    plataforma = forms.CharField(max_length=80)
    fechaDeInicio = forms.DateField()

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['user', 'imagen']

class ContactoFormumlario(forms.Form):
    correo = forms.EmailField(required=True)
    nombre= forms.CharField(required=True, max_length=30)
    apellido = forms.CharField(required=True, max_length=30)
    asunto = forms.CharField(required=True, max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea, required=True, max_length=10000)