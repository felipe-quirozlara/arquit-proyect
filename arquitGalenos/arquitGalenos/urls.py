"""arquitGalenos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('hora/', toma_hora_page, name="toma_hora_page"),
    path('doctores/<str:pk>', doctores, name="doctores_pages"),
    path('confirmacion/<str:pk>', confirmacion, name="confirmacion_page"),
    path('cancelar/', cancelar_page, name="cancelar_page"),
    path('confirmacion/cancelar/<str:pk>', confirm_cancelar, name="confirm_cancelar_page"),
    path('secretaria/', secretaria_page, name="secretaria_page" ),
    path('secretaria/agregar/hora', agregar_hora_page, name="agregar_hora_page" ),
    path('secretaria/agregar/medico', agregar_medico_page, name="agregar_medico_page" ),
    path('secretaria/agregar/disponibilidad', agregar_disponibilidad_page, name="agregar_disponibilidad_page" ),



    path('secretaria/quitar/hora', quitar_hora_page, name="quitar_hora_page" ),


    path('logout/', logout_user, name='logout_user'),
    path('login/', login_page, name='login_page'),
    path('admin/', admin.site.urls),
]
