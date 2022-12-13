from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . models import Customer

class LoginForm(forms.Form):
    username = forms.CharField(      
        required=True,
        widget=forms.TextInput(
           attrs={               
                "placeholder":"Nombre de usuario",
                "class":"form__input",
                "autocomplete":"off"
            } 
        )
    )

    password = forms.CharField(        
        required=True,
        widget=forms.PasswordInput(
           attrs={              
                "placeholder":"Contaseña",
                "class":"form__input",
                # "autocomplete":"off"
            } 
        )
    )

class SignUpForm(UserCreationForm):

    username = forms.CharField(
        # label='Username',
        required=True,
        widget=forms.TextInput(
           attrs={
                "placeholder":"Usuario",
                "class":"form__input",
                "value":"",
            } 
        )
    )

    email = forms.EmailField(
        # label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Email",
                "class":"form__input"
            } 
        )
    )

    password1 = forms.CharField(
        # label='Password1',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Contraseña",
                "class":"form__input"
            } 
        )
    )

    password2 = forms.CharField(
        # label='Password2',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Contraseña",
                "class":"form__input"
            } 
        )
    )

    class Meta:
        model= User
        fields = ('username','email','password1','password2')

class CustomerForm(forms.ModelForm):

    name = forms.CharField(
        # label='Name',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre",
                "class":"form__input",
            }
        )
    )

    last_name = forms.CharField(
        # label='Last name',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Apellidos",
                "class":"form__input",
            }
        )
    )

    cel = forms.CharField(
        # label='Cel',
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Cel",
                "class": "form__input",
            }
        )
    )

    imagen=forms.ImageField()
    
    



