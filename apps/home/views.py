from django.shortcuts import render
from django.http import JsonResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home/home.html',{})





# VISTAS PARA PETICIONES AJAX#






