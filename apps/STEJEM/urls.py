from django.urls import path, re_path
from . import views

urlpatterns = [
    path('search_STEJEM/', views.ventana_STJEM, name='STEJEM'),
    path('search_STEJEM/salas/areas', views.get_area_salas),
    path('search_STEJEM/juzgados/distritos', views.get_distrito_Juzgado),
    path('search_STEJEM/juzgados/distritos/<int:distrito_id>', views.get_areas_juzgados),
]