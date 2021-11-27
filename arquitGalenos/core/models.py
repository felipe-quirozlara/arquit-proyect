from django.db import models
import datetime
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    p_apellido = models.CharField(max_length=20)
    m_apellido = models.CharField(max_length=20)
    rut = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return str(self.nombre + ' ' + self.p_apellido)

class Paciente(Persona):

    MUJER = 'MJ'
    HOMBRE = 'HM'

    SEXO = [
        (MUJER, 'Mujer'),
        (HOMBRE, 'Hombre')
    ]

    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=2,choices=SEXO)

class Medico(Persona):

    FAMILIAR = "FM"
    PEDIATRIA = "PD"
    INTERNA = "IN"
    PSIQUIATRIA = "SQ"
    ORTOPEDIA = "OP"
    OFTALMOLOGIA = "OF"
    GENERAL = "GN"
    DERMATOLOGIA = "DT"
    CARDIOLOGIA = "CD"

    ESPECIALIDAD = [
        (FAMILIAR, 'Familiar'),
        (PEDIATRIA, 'Pediatría'),
        (INTERNA, 'Interna'),
        (PSIQUIATRIA, 'Psiquiatría'),
        (ORTOPEDIA, 'Ortopedia'),
        (OFTALMOLOGIA, 'Oftalmología'),
        (GENERAL, 'General'),
        (DERMATOLOGIA, 'Dermatología'),
        (CARDIOLOGIA, 'Cardiología')
    ]

    especialidad = models.CharField(max_length=2,choices=ESPECIALIDAD)

class Disponibilidad(models.Model):
    medico = models.OneToOneField(Medico, null=True, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return str(self.medico)



    def save(self, *args, **kwargs):

        fecha = datetime.date.today()
        fin_fecha = fecha + datetime.timedelta(days=7)
        hora_inicio = self.hora_inicio.hour
        hora_fin = self.hora_fin.hour
        delta = datetime.timedelta(days=1)        

        while fecha <= fin_fecha:
            b = hora_inicio
            while b < hora_fin:
                new_hora = datetime.time(b,0)
                # creación de hora medica
                h = Hora(medico=self.medico, hora_inicio=new_hora, fecha=fecha)
                h.save()
                b += 1

            fecha += delta
        
        super().save(*args, **kwargs)  # Call the "real" save() method.
    

class Hora(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    fecha = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return str(self.medico.nombre + ' ' + self.medico.p_apellido + ' ' + str(self.fecha)+ ' ' + str(self.hora_inicio))

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    hora = models.ForeignKey(Hora, on_delete=models.SET_NULL, null=True, blank=True)
    habilitada = models.BooleanField(default=True)