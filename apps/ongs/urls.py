from django.urls import path
from . import views

app_name = 'ongs'

urlpatterns = [
    path('', views.list_ongs, name='list_ongs'),
    path('adicionar/', views.add_ong, name='add_ong'),
    path('editar/<int:id_ong>/', views.edit_ong, name='edit_ong'),
    path('excluir/<int:id_ong>/', views.delete_ong, name='delete_ong'),
]