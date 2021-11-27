from django.db import models
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import model_to_dict
from .models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class HoraForm(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ['medico', 'hora_inicio', 'fecha']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = '__all__'

