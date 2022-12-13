from django import forms
from django.contrib.auth.models import User
from ..authentication.models import Customer

class editPerfilUserForm(forms.ModelForm):

    username = forms.CharField(
        # label='Username',
        required=True,
        widget=forms.TextInput(
           attrs={
                "placeholder":"Usuario",
                "class":"form__input",
                "name":"username"
            } 
        )
    )

    email = forms.EmailField(
        # label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Email",
                "class":"form__input",
                "name":"email"
            } 
        )
    )

    password1 = forms.CharField(
        # label='Password1',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Contraseña",
                "class":"form__input",
                "name":"password1"
            } 
        )
    )

    password2 = forms.CharField(
        # label='Password2',
        required=True,
        widget=forms.PasswordInput(
           attrs={
                "placeholder":"Contraseña",
                "class":"form__input",
                "name":"password2"
            } 
        )
    )

    class Meta:
        model= User
        fields = ('username','email','password1','password2')

class editPerfilCustomerForm(forms.Form):
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

