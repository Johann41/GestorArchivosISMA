from django.urls import path
from . import views


urlpatterns = [
    path('auth/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('password/', views.password, name='password'),
]
