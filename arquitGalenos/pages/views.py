from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Medico, Hora, Cita, Paciente
from core.forms import PacienteForm, HoraForm, MedicoForm, DisponibilidadForm, CitaForm
from core.decorators import usuarios_permitiado, usuario_identificado
from datetime import *
# Create your views here.
def home_page(request):

    context = {}
    
    return render(request,'pages/home.html', context)

def toma_hora_page(request):

    context = {}
    if request.method == "POST":
        b = request.POST['especialidad']
        return redirect('doctores_pages', pk=b)
    else:
        print("error")
    

    return render(request,'pages/tomar_hora.html', context)

def doctores(request, pk):
    context = {}

    try:
        doctores = Medico.objects.filter(especialidad=pk)
        doc_list = []
        startdate = date.today()
        enddate = startdate + timedelta(days=16)
        for doctor in doctores:
            horas = Hora.objects.filter(medico=doctor, disponible=True).filter(fecha__range=[startdate, enddate])
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
    else:
        print("error")

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
            else:
                print("error")  
    else:
        print("error")

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
        print("error")

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
    else:
        print("error")

    return render(request, 'pages/conf_cancel.html', context)

def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            print("error al indentificar")
    else:
            print("error")


    return render(request, 'pages/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page') 

@login_required(login_url="login_page")
@usuarios_permitiado(roles_permitidos=['secretaria'])
def secretaria_page(request):
    context = {}
    return render(request, 'pages/secretaria.html', context)

@login_required(login_url="login_page")
@usuarios_permitiado(roles_permitidos=['secretaria'])
def agregar_hora_page(request):
    context = {}
    form = HoraForm()
    context["form"] = form

    if request.method == 'POST':
        form = HoraForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("error")
    else:
            print("error")

    return render(request, 'pages/secretaria/agregar_hora.html', context)

@login_required(login_url="login_page")
@usuarios_permitiado(roles_permitidos=['secretaria'])
def quitar_hora_page(request):
    context = {}

    try:
        doctores = Medico.objects.all()
        startdate = date.today()
        enddate = startdate + timedelta(days=16)
        doc_list = []
        for doctor in doctores:
            horas = Hora.objects.filter(medico=doctor, disponible=True).filter(fecha__range=[startdate, enddate])
            grouped = dict()
            for hora in horas:
                grouped.setdefault(hora.fecha, []).append(hora)  
            obj = {"doctor": doctor, "horas": grouped}
            doc_list.append(obj)
            
            
        context['doctores'] = doc_list
    except:
        context['doctores'] = "sin doctores"
        context["horas"] = "sin horas"

    if request.method == 'POST':
        pk = request.POST["hora"]
        hora = Hora.objects.get(id=pk)
        hora.disponible = False
        hora.save()
        return redirect('secretaria_page')
    else:
            print("error")
    return render(request, 'pages/secretaria/quitar_hora.html', context)

@login_required(login_url="login_page")
@usuarios_permitiado(roles_permitidos=['secretaria'])
def agregar_medico_page(request):
    context = {}
    form = MedicoForm()
    context["form"] = form
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("error")
    else:
            print("error")
    return render(request, 'pages/secretaria/agregar_medico.html', context)

@login_required(login_url="login_page")
@usuarios_permitiado(roles_permitidos=['secretaria'])
def agregar_disponibilidad_page(request):
    context = {}
    form = DisponibilidadForm()
    context["form"] = form
    if request.method == 'POST':
        form = DisponibilidadForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("error")
    else:
            print("error")

    return render(request, 'pages/secretaria/agregar_disponibilidad.html', context)

@login_required(login_url="login_page")
@usuarios_permitiado(roles_permitidos=['secretaria'])
def modificar_cita_page(request):
    context = {}
    
    citas = Cita.objects.filter(habilitada=True)

    context["citas"] = citas

    return render(request, 'pages/secretaria/modificar_hora.html', context)

@login_required(login_url="login_page")
@usuarios_permitiado(roles_permitidos=['secretaria'])
def update_cita_page(request, pk):
    context = {}
    cita = Cita.objects.get(id=pk)
    form = CitaForm(instance=cita)

    context["form"] = form

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("error")
    else:
            print("error")

    return render(request, 'pages/secretaria/update_cita.html', context)