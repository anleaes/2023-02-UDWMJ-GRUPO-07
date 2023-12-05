from django.urls import path
from . import views

app_name = 'adocoes'

urlpatterns = [
    path('', views.list_adocoes, name='list_adocoes'),
    path('adicionar/', views.add_adocao, name='add_adocao'),
    path('editar/<int:id_adocao>/', views.edit_adocao, name='edit_adocao'),
    path('excluir/<int:id_adocao>/', views.delete_adocao, name='delete_adocao'),
]