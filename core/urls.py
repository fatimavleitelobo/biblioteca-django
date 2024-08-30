from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categoria_list_create, name='categoria-list-create'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria-detail'),
    path('autores/', views.autor_list_create, name='autor-list-create'),
    path('autores/<int:pk>/', views.autor_detail, name='autor-detail'),
    path('livros/', views.livro_list_create, name='livro-list-create'),
    path('livros/<int:pk>/', views.livro_detail, name='auto-detail')
]