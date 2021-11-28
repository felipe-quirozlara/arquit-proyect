from django.db import models
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import model_to_dict
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': DateInput()
        }

class HoraForm(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ['medico', 'hora_inicio', 'fecha']
        widgets = {
            'fecha': DateInput(),
            'hora_inicio': TimeInput()
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = '__all__'
        widgets = {
            'hora_inicio': TimeInput(),
            'hora_fin': TimeInput(),
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'