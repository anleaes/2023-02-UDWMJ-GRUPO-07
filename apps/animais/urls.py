from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('', views.list_animais, name='list_animais'),
    path('adicionar/', views.add_animal, name='add_animal'),
    path('editar/<int:id_animal>/', views.edit_animal, name='edit_animal'),
    path('excluir/<int:id_animal>/', views.delete_animal, name='delete_animal'),
    path('buscar/', views.search_animais, name='search_animais'),
]