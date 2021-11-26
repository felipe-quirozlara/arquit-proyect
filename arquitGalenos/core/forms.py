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