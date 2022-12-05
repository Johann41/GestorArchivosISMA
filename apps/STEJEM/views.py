from django.shortcuts import render
from django.http import JsonResponse
from . models import areas_Juzgado, areas_Salas, distrito_Juzgado

# Create your views here.

def ventana_STJEM(request):

    fomulario_salas = ''
    fomulario_juzgados = ''

    if request.POST.get('buscador')=='salas':        
        fomulario_salas = "s"
        print('salas')

    elif request.POST.get('buscador')=='juzgado':
        print('juz')
        fomulario_juzgados = "j"

    return render(request, 'home/STEJEM.html',{'salas':fomulario_salas, 'juzgado':fomulario_juzgados})

def get_area_salas(request):
    areas = list(areas_Salas.objects.values())

    if(len(areas) > 0 ):
        data = {'msg':"Success", 'areas':areas}
    else:
        data = {'msg':"Not found"}
    
    return JsonResponse(data)

def get_distrito_Juzgado(request):
    distritos = list(distrito_Juzgado.objects.values())

    if(len(distritos) > 0 ):
        data = {'msg':"Success", 'distritos':distritos}
    else:
        data = {'msg':"Not found"}
    
    return JsonResponse(data)

def get_areas_juzgados(request, distrito_id):
    areas = list(areas_Juzgado.objects.filter(distrito_id=distrito_id).values())

    if(len(areas) > 0 ):
        data = {'msg':"Success", 'areas':areas}
    else:
        data = {'msg':"Not found"}
    
    return JsonResponse(data)
