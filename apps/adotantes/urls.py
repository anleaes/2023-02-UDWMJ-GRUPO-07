from django.urls import path
from . import views

app_name = 'adotantes'

urlpatterns = [
    path('', views.list_adotantes, name='list_adotantes'),
    path('adicionar/', views.add_adotante, name='add_adotante'),
    path('editar/<int:id_adotante>/', views.edit_adotante, name='edit_adotante'),
    path('excluir/<int:id_adotante>/', views.delete_adotante, name='delete_adotante'),
]