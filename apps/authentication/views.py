from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):  
    return  render(request, 'authentication/login.html',{})

def signup(request):  
    return  render(request, 'authentication/signup.html',{})

def password(request):  
    return  render(request, 'authentication/restore_password.html',{})