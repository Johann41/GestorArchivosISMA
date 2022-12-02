from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def ventana_AGRARIO(request):
    return render(request, 'home/AGRARIO.html',{})

def get_tribunales_AGRERIOS(request):

    tribunales = list(Tribunales_AGRARIOS.objects.values())

    if(len(tribunales)>0):
        data = {'msg':"Success", 'tribunales':tribunales}
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
