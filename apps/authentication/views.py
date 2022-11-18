from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm
from .models import Perfil
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
    # model = Perfil 
    msg = None
    formulario = SignupForm(request.POST or None)
    if request.method =='POST':     
        if formulario.is_valid():

            username = formulario.cleaned_data.get('username')
            cel = formulario.cleaned_data.get('cel')
            password = formulario.cleaned_data.get('password1') 
            password_hash = User.check_password()
            print(password_hash)

            User.check_password
            
            user = User.objects.create_user(username=username, password=password)  
            user_auth =  authenticate(username = username, password=password)

            # print(user)
            nuevo_perfil = Perfil.objects.create(usuario=username, cel=cel)
            login(request,user_auth)         
            formulario.save()   
            return redirect('home') 

            # # if user is not None:
                
            # #     new_formulario.user=user
            # #     new_formulario.save()
            # #     return redirect('home') 

            # else:
            #     msg = "Error al autentificar"

        else:  
            msg = "Error"                                        
            form = SignupForm()
        
        
    return  render(request, 'authentication/signup.html',{"form":formulario, "msg":msg})

def password_view(request): 

    return  render(request, 'authentication/restore_password.html',{})