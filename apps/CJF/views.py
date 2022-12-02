from django.shortcuts import render

# Create your views here.
def ventana_CJF(request):
    return render(request, 'home/CJF.html',{})

