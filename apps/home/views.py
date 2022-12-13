from django.shortcuts import render, redirect
from .forms import editPerfilCustomerForm, editPerfilUserForm
from ..authentication.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='auth_login')
def home(request):
    return render(request, 'home/home.html',{})


@login_required(login_url='auth_login')
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


@login_required(login_url='auth_login')
def editar_perfil(request, id):
    msg=None
    # user = User.objects.filter(id=id)
    customer = Customer.objects.get(user_id=id)
    # form_django = editPerfilUserForm(initial={'username':user.username, 'email':user.email})
    form_custumer = editPerfilCustomerForm(initial={'cel':customer.cel, 'name': customer.name, 'last_name':customer.last_name, 'imagen':customer.imagen})

    if request.method == "POST":
        form_custumer = editPerfilCustomerForm(request.POST, request.FILES)
        
        if form_custumer.is_valid():
            customer.cel = form_custumer.cleaned_data["cel"]
            customer.name = form_custumer.cleaned_data["name"]
            customer.last_name = form_custumer.cleaned_data["last_name"]
            customer.imagen = form_custumer.cleaned_data["imagen"]
            customer.save()
            return redirect('perfil')
        else:
            print('error')

    context = {
        "msg":msg,
        # "form_django":form_django,
        "form_customer":form_custumer
    }

    return render(request, 'home/editarperfil.html',context)

# VISTAS PARA PETICIONES AJAX#






