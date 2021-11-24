from django.contrib import admin

from .models import Disponibilidad, Hora, Medico, Paciente, Persona

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Disponibilidad)
admin.site.register(Hora)
