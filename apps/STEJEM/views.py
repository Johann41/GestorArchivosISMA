from django.shortcuts import render

# Create your views here.
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