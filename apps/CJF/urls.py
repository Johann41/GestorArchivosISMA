from django.urls import path
from . import views

urlpatterns = [
    path('search_CJF/', views.ventana_CJF, name='CJF'),
    path('search_CJF/circuitos/', views.get_circuito),
    path('search_CJF/organo_jurisdiccional/<int:id>', views.get_organoJurisdiccional),
]