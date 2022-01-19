from django import forms


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