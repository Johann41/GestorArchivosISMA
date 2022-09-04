from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='auth_login'),
    path('signup/', views.signup, name='auth_signup'),
    path('password/', views.password, name='auth_password'),
]
