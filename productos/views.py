from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Paleta
# Create your views here.

def paletas(request):
    return HttpResponse("esta es la vista de paletas")

class Paletas(ListView):
    model = Paleta
    template_name = "paletas/listado_de_paletas.html"
    context_object_name = "paletas"
    
class CrearPaleta(CreateView):
    model = Paleta
    template_name = "paletas/listado_de_paletas.html"
    success_url = ""
    fields = ["marca", "descripcion", "fecha"]
    
    
class EditarPaleta(UpdateView):        
    ...