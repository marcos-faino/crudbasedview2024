from django.urls import path
from core import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('add/categoria', views.CategoriaCreateView.as_view(),
         name='addCategoria'),
    path('listar/categorias', views.CategoriaListView.as_view(),
         name='listarCategorias'),
    path('atualizar/categoria/<int:pk>', views.CategoriaUpdateView.as_view(),
         name='atualizaCategoria'),
    path('excluir/categoria/<int:pk>', views.CategoriaDeleteView.as_view(),
         name='excluiCategoria'),
]