from django.urls import path
from . import views

urlpatterns = [
    path('search_STEJEM/', views.ventana_STJEM, name='STEJEM'),
    path(r'search_STEJEM/.+/salas/area', views.get_area_salas),
    path('search_STEJEM/juzgado/distrito', views.get_distrito_Juzgado),
    path('search_STEJEM/juzado/distrito/<int:distrito_id>', views.get_areas_juzgados),
]