from django.shortcuts import render
from django.http import JsonResponse
from .models import Circuito, Organo_Jurisdiccional

# Create your views here.
def ventana_CJF(request):
    return render(request, 'home/CJF.html',{})

def get_circuito(request):
    circuito = list(Circuito.objects.values())

    if(len(circuito) > 0):
        data = {'msg':"Success", 'circuitos':circuito}
    else:
        data = {'msg':"Not found"}

    return JsonResponse(data)


def get_organoJurisdiccional(request, id):
    organo_j = list(Organo_Jurisdiccional.objects.filter(instancia_id=id).values())

    if(len(organo_j) > 0):
        data = {'msg':"Success", 'organos_j': organo_j}
    else:
        data = {'msg':"Not found"}

    return JsonResponse(data)


