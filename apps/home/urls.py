from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search_TJAM/', views.ventana_TJAM, name='TJAM'),
    path('search_STEJEM/', views.ventana_STJEM, name='STEJEM'),
    path('search_AGRARIOS/', views.ventana_AGRARIO, name='AGRARIOS'),
]
