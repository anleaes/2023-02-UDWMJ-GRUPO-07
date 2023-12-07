from django.urls import path
from . import views

app_name = 'adocaoanimais'

urlpatterns = [
    path('', views.list_adocaoanimais, name='list_adocaoanimais'),
    path('adicionar/', views.add_adocaoanimal, name='add_adocaoanimal'),
    path('editar/<int:id_adocaoanimal>/', views.edit_adocaoanimal, name='edit_adocaoanimal'),
    path('excluir/<int:id_adocaoanimal>/', views.delete_adocaoanimal, name='delete_adocaoanimal'),
]
