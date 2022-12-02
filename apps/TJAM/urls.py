from django.urls import path
from . import views

urlpatterns = [
    path('search_TJAM/', views.ventana_TJAM, name='TJAM'),
    path('search_TJAM/instancias/', views.get_instancia_TJAM),
    path('search_TJAM/numeros/<int:instancia_id>', views.get_numero_TJAM),
    path('search_TJAM/tipos/<int:instancia_id>', views.get_tipo_TJAM),
]
