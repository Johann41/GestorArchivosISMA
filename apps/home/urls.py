from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search_TJAM/', views.ventana_TJAM, name='TJAM'),
    path('search_STEJEM/', views.ventana_STJEM, name='STEJEM'),
    path('search_AGRARIOS/', views.ventana_AGRARIO, name='AGRARIOS'),
    path('search_CJF/', views.ventana_CJF, name='CJF'),

    # URL DE AJAX #

    path('search_TJAM/instancias/', views.get_instancia_TJAM),
    path('search_TJAM/numeros/<int:instancia_id>', views.get_numero_TJAM),
    path('search_TJAM/tipos/<int:instancia_id>', views.get_tipo_TJAM),

    path('search_AGRARIOS/tribunales/', views.get_tribunales_AGRERIOS)


]
