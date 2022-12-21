from django.shortcuts import render
from .models import Miembro,Colaborador
from django.http import HttpResponse
from datetime import datetime 
from django.urls import reverse_lazy
import datetime
from django.template import Template, Context
from django.template import loader
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .forms import ColaboradorForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def saludar(request):
    return HttpResponse("hola mundo!")

def segunda_vista(request):
    return HttpResponse ("Ya entendi esto parece ser muy simple")

def dia_de_hoy(request):
    dia= datetime.datetime.today()
    cadena=f"hos es {dia}"
    return HttpResponse(f"hoy es {cadena}")

def saludo_con_nombre(request,nombre):
    return HttpResponse(f"Hola {nombre} como estas?")

def calcula_anio_nacimiento(request,edad):
    anio_actual= datetime.datetime.today().year
    anio_nacimiento= anio_actual - int(edad)
    return HttpResponse(f"<h1> Usted nacio en el año{anio_nacimiento}<h1>")

# FUNCIONES DE BASE DE DATOS

def Principal(request):
    teste={"Hola":"Markos"}
    template2= loader.get_template("principal.html")
    documento2= template2.render(teste)
    return HttpResponse(documento2)

def Colaboradores_site(request):
    teste={"Hola":"Markos"}
    template= loader.get_template("Colaborador.html")
    documento= template.render(teste)
    return HttpResponse(documento)

def Sitio_web(request):

    diccionario={"nombre":"Markos","apellido":"Mavarez","edad":str(28),"lista_de_notas":[10,9,5,7,8]}
    template= loader.get_template("template1.html")
    documento= template.render(diccionario)
    return HttpResponse(documento)



# Ingresos de datos a DB 

def familiar(request):

    familiar_nuevo= Miembro(nombre="enmanuel", apellido= "Mavarez",edad=30, afinidad= "hermano", fecha_nacimiento= datetime.date(1995, 12, 25))
    familiar_nuevo.save()
    cadena_texto= f"Familiar Guardado: Nombre: {familiar_nuevo.nombre}  ,__Apellido: {familiar_nuevo.apellido}  ,__Edad: {familiar_nuevo.edad}  ,__afinidad: {familiar_nuevo.afinidad}  ,__fecha: {familiar_nuevo.fecha_nacimiento}"
    return HttpResponse(cadena_texto)

def Ing_colaborador(request):

    colaborador_nuevo= Colaborador(nombre="enmanuel", apellido= "Mavarez",dni=95711470, cargo= "programador", fecha_ingreso= datetime.date(2014, 12, 25))
    colaborador_nuevo.save()
    cadena_texto= f"colaborador Guardado: Nombre: {colaborador_nuevo.nombre}  ,__Apellido: {colaborador_nuevo.apellido}  ,__dni: {colaborador_nuevo.dni}  ,__cargo: {colaborador_nuevo.cargo}  ,__fecha_ingreso: {colaborador_nuevo.fecha_ingreso}"
    return HttpResponse(cadena_texto)


# ingreso desde formularios

@csrf_exempt
def Familiar_site(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        edad=request.POST["edad"]
        afinidad=request.POST["afinidad"]
        fecha_nacimiento=request.POST["fecha_nacimiento"]
        familiar_nuevo= Miembro(nombre= nombre, apellido= apellido,edad=edad, afinidad= afinidad, fecha_nacimiento= fecha_nacimiento)
        familiar_nuevo.save()
        return render(request,"Principal.html",{"mensaje":"Familiar guardado Correctamente"})
    else:
        teste={"Hola":"Markos"}
        template= loader.get_template("familiar.html")
        documento= template.render(teste)
        return HttpResponse(documento) 

@csrf_exempt
def Colaborador_site(request):
    if request.method=="POST":
        pass
    else:
        formulario= ColaboradorForm()
        return render (request, "Colaborador.html", {"form_colaborador": formulario})     