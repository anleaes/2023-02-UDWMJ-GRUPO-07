from django.urls import path
from . import views

app_name = 'doadores'

urlpatterns = [
    path('', views.list_doadores, name='list_doadores'),
    path('adicionar/', views.add_doador, name='add_doador'),
    path('editar/<int:id_doador>/', views.edit_doador, name='edit_doador'),
    path('excluir/<int:id_doador>/', views.delete_doador, name='delete_doador'),
]