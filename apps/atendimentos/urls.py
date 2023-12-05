from django.urls import path
from . import views

app_name = 'Atendimentos'

urlpatterns = [
    path('', views.list_atendimentos, name='list_atendimentos'),
    path('adicionar/', views.add_atendimento, name='add_atendimento'),
    path('editar/<int:id_atendimento>/', views.edit_atendimento, name='edit_atendimento'),
    path('excluir/<int:id_atendimento>/', views.delete_atendimento, name='delete_atendimento'),
]