from django.urls import path
from . import views

app_name = 'veterinarios'

urlpatterns = [
    path('', views.list_veterinarios, name='list_veterinarios'),
    path('adicionar/', views.add_veterinario, name='add_veterinario'),
    path('editar/<int:id_veterinario>/', views.edit_veterinario, name='edit_veterinario'),
    path('excluir/<int:id_veterinario>/', views.delete_veterinario, name='delete_veterinario'),
]