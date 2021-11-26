from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from core.models import Medico, Hora, Cita, Paciente
from core.forms import PacienteForm

# Create your views here.
def home_page(request):

    context = {}
    if request.method == "POST":
        b = request.POST['especialidad']
        return redirect('doctores_pages', pk=b)
    

    return render(request,'pages/tomar_hora.html', context)

def doctores(request, pk):
    context = {}

    try:
        doctores = Medico.objects.filter(especialidad=pk)
        doc_grouped = dict()
        doc_list = []
        for doctor in doctores:
            horas = Hora.objects.filter(medico=doctor, disponible=True)
            grouped = dict()
            for hora in horas:
                grouped.setdefault(hora.fecha, []).append(hora)  
            obj = {"doctor": doctor, "horas": grouped}
            doc_list.append(obj)
            
            
        context['doctores'] = doc_list
    except:
        context['doctores'] = "sin doctores"
        context["horas"] = "sin horas"

    if request.method == "POST":
        pk = request.POST["hora"]
        return redirect('confirmacion_page', pk=pk)

    return render(request,'pages/docts.html', context)

def confirmacion(request, pk):
    context = {}
    form = PacienteForm()

    hora = Hora.objects.get(id=pk)

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        try:
            rut = request.POST["rut"]
            paciente = Paciente.objects.get(rut=rut)
            hora.disponible = False
            hora.save()
            Cita.objects.create(
                paciente = paciente,
                hora = hora
            )
            return redirect('home_page')
        except:
            if form.is_valid():
                paciente = form.save()
                hora.disponible = False
                hora.save()
                Cita.objects.create(
                    paciente = paciente,
                    hora = hora
                )
                return redirect('home_page')


    context["form"] = form
    context["hora"] = hora
    return render(request, 'pages/conf.html', context)

def cancelar_page(request):
    context = {}

    if request.method == 'POST':
        rut = request.POST['rut']
        paciente = Paciente.objects.get(rut=rut)
        citas =  Cita.objects.filter(paciente=paciente, habilitada=True)

        context["citas"] = citas
    else:
        pass

    return render(request, 'pages/cancel.html', context)

def confirm_cancelar(request, pk):
    context = {}

    cita = Cita.objects.get(id=pk)

    context["cita"] = cita

    if request.method == 'POST':
        cita.habilitada = False
        cita.save()
        hora = Hora.objects.get(id=cita.hora.id)
        hora.disponible = True
        hora.save()       

    return render(request, 'pages/conf_cancel.html', context)