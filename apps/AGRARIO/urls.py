from django.urls import path
from . import views

urlpatterns = [
    path('search_AGRARIOS/', views.ventana_AGRARIO, name='AGRARIOS'),
    path('search_AGRARIOS/tribunales/', views.get_tribunales_AGRERIOS)
]