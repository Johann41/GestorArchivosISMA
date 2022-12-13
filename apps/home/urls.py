from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/',views.perfil, name='perfil'),
    path('editar_perfil/<int:id>',views.editar_perfil, name='editarperfil'),
]
