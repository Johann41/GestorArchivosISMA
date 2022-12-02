from django.urls import path
from . import views

urlpatterns = [
    path('search_STEJEM/', views.ventana_STJEM, name='STEJEM'),
]