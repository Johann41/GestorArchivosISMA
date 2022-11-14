from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(      
        required=True,
        widget=forms.TextInput(
           attrs={               
                "placeholder":"usuario",
                "class":"form__input"
            } 
        )
    )

    password = forms.CharField(        
        required=True,
        widget=forms.PasswordInput(
           attrs={              
                "placeholder":"contaseña",
                "class":"form__input"
            } 
        )
    )

class SignupForm(UserCreationForm):

    name = forms.CharField(
        label='Nombre(s)',
        required=True,
        widget=forms.TextInput(
           attrs={             
                "class":"form__input"
            } 
        )
    )

    last_name = forms.CharField(
        label='Apellidos',
        required=True,
        widget=forms.TextInput(
           attrs={              
                "class":"form__input"
            } 
        )
    )

    username = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        widget=forms.TextInput(
           attrs={              
                "class":"form__input"
            } 
        )
    )
    
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
           attrs={     
                "placeholder":"ejemplo@gmail.com",        
                "class":"form__input"
            } 
        )
    )

    cel = forms.CharField(
        label='Celular',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"443333536235",
                "class":"form__input"
            } 
        )
    )

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "class":"form__input"
            } 
        )
    )

    password2 = forms.CharField(
        label='Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(
           attrs={          
                "class":"form__input"
            } 
        )
    )

    class Meta:
        model = User
        fields=('name','last_name','username','email','cel','password1','password2')