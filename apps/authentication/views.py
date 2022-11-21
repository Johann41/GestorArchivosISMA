from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import LoginForm, CustomerForm, SignUpForm
from django.contrib import messages

# Create your views here.

def login_view(request): 

    msg = None
    form = LoginForm(request.POST or None)

    if request.user.is_authenticated:       
        return redirect('home')

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = "usuario o contraseña incorrecta"
        else:
            print('no es valido')

    return  render(request, 'authentication/login.html',{"form":form, "msg":msg})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)   
    return redirect('auth_login')

def signup_view(request):
    
    signup_form = SignUpForm(request.POST or None, prefix='signup')
    customer_form = CustomerForm(request.POST or None, prefix='customer')
    msg = None

    if request.method == "POST":
        if signup_form.is_valid() and customer_form.is_valid():

            user_form = signup_form.save()
            new_customer = customer_form.save(commit=False)
            
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                new_customer.user = user
                new_customer.save()
                return redirect('home')
            else:
                msg = "Erro al autentificar"

        else:
            msg = 'Error al registrar usuario: '
    
    context = {
        "signup_form": signup_form,
        "customer_form": customer_form,
        "msg": msg,
    }

        
    return  render(request, 'authentication/signup.html',context)

def password_view(request): 

    return  render(request, 'authentication/restore_password.html',{})