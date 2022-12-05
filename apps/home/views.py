from django.shortcuts import render
from .forms import editPerfilCustomerForm, editPerfilUserForm
from ..authentication.models import Customer
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home/home.html',{})

def perfil(request):
    msg=None
    current_user = request.user  
    django_profile = User.objects.filter(username=current_user)
    perfil = Customer.objects.filter(user=current_user).values() 

    context = {       
        "msg": msg,
        "datos_user":perfil,
        "django_profile":django_profile,
    }

    return render(request, 'home/perfil.html',context)

def editar_perfil(request, pk):
    msg=None
    current_user = request.user  
    editUser_form = editPerfilCustomerForm(request.POST or None, prefix='user')
    editCustomer_form = editPerfilUserForm(request.POST or None, prefix='customer')
    django_profile = User.objects.filter(username=current_user)
    perfil = Customer.objects.filter(user=current_user).values() 
    
    if request.method == "POST":
        
        if editar_perfil.is_valid() and editar_perfil.is_valid():
            editUser_form.save()
            editCustomer_form.save()
        else:
          msg="Error al enviar datos"  

    context = {
        "perfilUser_form": editUser_form,
        "perfilCustomer_form": editUser_form,
        "msg": msg,
        "datos_user":perfil,
        "django_profile":django_profile,
    }

    return render(request, 'home/perfil.html',context)

# VISTAS PARA PETICIONES AJAX#






