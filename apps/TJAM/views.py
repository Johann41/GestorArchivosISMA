
from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def ventana_TJAM(request):    
    return render(request, 'home/TJAM.html',{})


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