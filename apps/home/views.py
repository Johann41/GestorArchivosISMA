from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html',{})

def ventana_TJAM(request):
    return render(request, 'home/TJAM.html',{})

def ventana_STJEM(request):
    return render(request, 'home/STEJEM.html',{})

def ventana_AGRARIO(request):
    return render(request, 'home/AGRARIO.html',{})

def ventana_CJF(request):
    return render(request, 'home/CJF.html',{})

