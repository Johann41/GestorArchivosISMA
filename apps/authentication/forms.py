from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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

class SignupForm(forms.ModelForm):

    # name = forms.CharField(
       
    #     required=True,
    #     widget=forms.TextInput(
    #        attrs={             
    #             "class":"form__input"
    #         } 
    #     )
    # )

    # last_name = forms.CharField(
       
    #     required=True,
    #     widget=forms.TextInput(
    #        attrs={      
    #             "placeholder":"ejemplo@gmail.com",        
    #             "class":"form__input"
    #         } 
    #     )
    # )

    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
           attrs={        
                # "placeholder":"usuario",      
                "class":"form__input",
                # "autocomplete":"off"
            } 
        )
    )
    
    # mail = forms.EmailField(

    #     required=True,
    #     widget=forms.EmailInput(
    #        attrs={     
    #             "placeholder":"ejemplo@gmail.com",        
    #             "class":"form__input"
    #         } 
    #     )
    # )

    cel = forms.CharField(    
        max_length=30, 
        required=True,  
        widget=forms.TextInput(
            attrs={
                # "placeholder":"443333536235",
                "class":"form__input",
                "type":"number"
            } 
        )
    )

    password1 = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
           attrs={
                # "placeholder":"Ingrese su contraseña",
                "class":"form__input"
            } 
        )
    )

    password2 = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
           attrs={          
                # "placeholder":"Confirmar contraseña anterior",
                "class":"form__input"
            } 
        )
    )

    class Meta:
        model = User
        # fields=('name','last_name','username','email','cel','password1','password2')
        fields=('username','cel','password1','password2')
        help_texts = {k:"" for k in fields}