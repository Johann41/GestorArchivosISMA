from django.urls import path
from . import views

urlpatterns = [
    path('search_CJF/', views.ventana_CJF, name='CJF'),
]