from django.shortcuts import render, redirect
from datetime import datetime
from django.template import Template, Context, loader
import random

from inicio.models import Auto
from inicio.forms import CrearAutoFormulario, BuscarAuto, EditarAutoFormulario

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    #return HttpResponse("Bienvenido crack!")
    return render(request, "inicio/index.html")

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


def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca, modelo= modelo)
    auto.save()
    return render(request, "auto_templates/creacion.html", {"auto": auto})

def crear_auto_v2(request):
    #v1
    
    if request.method == "POST":
        ...
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            auto = Auto(marca=datos.get("marca"), modelo=datos.get("modelo"))#, anio=datos.get("anio"))
            auto.save()
            return redirect("inicio")
    formulario = CrearAutoFormulario()
    return render(request, "inicio/crear_auto_v2.html", {"formulario": formulario})
    
    # print("valor de request: ", request)
    # print("valor de GET: ", request.GET)
    # print("valor del post: ", request.POST)
    
def autos(request):
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data["marca"]
        autos = Auto.objects.filter(marca__icontains=marca)
    
    
    # auto = Auto.objects.all()
    return render(request, "inicio/autos.html", {"autos": autos, "formulario": formulario})
    
    
def eliminar_auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect("autos")

def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    formulario = EditarAutoFormulario(initial={"marca": auto.marca , "modelo": auto.modelo})# , "anio": auto.anio})
    
    if request.method == "POST":
        formulario = EditarAutoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            auto.marca = info["marca"]
            auto.modelo = info["modelo"]
            # auto.anio = info["anio"]
            
            auto.save()
            return redirect("autos")
    
    return render(request,'inicio/editar_auto.html',{'formulario': formulario,'auto': auto})


def ver_auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, "inicio/ver_auto.html", {"auto": auto})

