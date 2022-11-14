from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SignupForm

# Create your views here.

def login_view(request): 

    msg = None
    form = LoginForm(request.POST or None)

    if request.user.is_authenticated:       
        return redirect('home')

    if request.method == 'POST':
        print('peticion')

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
    form = SignupForm(request.POST or None)
    if request.method =='POST':
        
        if form.is_valid():
            form.save()
            return redirect('auth_login')
        else:
            form = SignupForm()

    return  render(request, 'authentication/signup.html',{"form":form})

def password_view(request): 

    return  render(request, 'authentication/restore_password.html',{})