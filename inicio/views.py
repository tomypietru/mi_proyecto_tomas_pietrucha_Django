from django.shortcuts import render
from datetime import datetime
from django.template import Template, Context, loader
import random


# Create your views here.

from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido crack!")

def template1(request,nombre, apellido, edad):
    fecha = datetime.now()
    suma = 4 + edad
    return HttpResponse(f"<h1>Mi Template 1</h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido} Edad: {edad}")


def template2(request, nombre, apellido, edad):
    archivo_abierto = open(r"C:\CoderHouse trabajos\Mi.Proyecto\templates\template2.html")
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    fecha = datetime.now
    
    datos = {
        "fecha": fecha, 
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
    }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse("")

def template3(request, nombre, apellido, edad):
    
    template = loader.get_template("template2.html")
    
    fecha = datetime.now
    
    datos = {
        "fecha": fecha, 
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
    }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def template4(request, nombre, apellido, edad):
    
    
    fecha = datetime.now
    
    datos = {
        "fecha": fecha, 
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
    }

    
    
    
    return render(request,"template2.html", datos)

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista,k=50)
    print(numeros)
    
    return render(request, "probando_if_for.html", {"numeros": numeros})