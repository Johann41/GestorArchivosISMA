from django.shortcuts import render
from django.http import JsonResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home/home.html',{})

def ventana_TJAM(request):    
    return render(request, 'home/TJAM.html',{})

def ventana_STJEM(request):

    fomulario_salas = ''
    fomulario_juzgados = ''

    if request.GET.get('buscador')=='salas':        
        fomulario_salas = "s"
        print('salas')

    elif request.GET.get('buscador')=='juzgado':
        print('juz')
        fomulario_juzgados = "j"

    return render(request, 'home/STEJEM.html',{'salas':fomulario_salas, 'juzgado':fomulario_juzgados})

def ventana_AGRARIO(request):
    return render(request, 'home/AGRARIO.html',{})

def ventana_CJF(request):
    return render(request, 'home/CJF.html',{})


# VISTAS PARA PETICIONES AJAX#

def get_instancia_TJAM(request):
    instancia = list(TJAM_instancia.objects.values())

    if(len(instancia) > 0):
        data = {'msg':"Success", 'instancias':instancia}
    else:
        data = {'msg':"Not found"}

    return JsonResponse(data)


def get_numero_TJAM(request, instancia_id):
    numero = list(TJAM_numero.objects.filter(instancia_id=instancia_id).values())

    if(len(numero) > 0):
        data = {'msg':"Success", 'numeros':numero}
    else:
        data = {'msg':"Not found"}

    return JsonResponse(data)


def get_tipo_TJAM(request, instancia_id):
    tipo = list(TJAM_tipo.objects.filter(instancia_id=instancia_id).values())

    if(len(tipo) > 0):
        data = {'msg':"Success", 'tipos':tipo}
    else:
        data = {'msg':"Not found"}

    return JsonResponse(data)


def get_tribunales_AGRERIOS(request):

    tribunales = list(Tribunales_AGRARIOS.objects.values())

    if(len(tribunales)>0):
        data = {'msg':"Success", 'tribunales':tribunales}
    else:
       data = {'msg':"Not found"}

    return JsonResponse(data) 

