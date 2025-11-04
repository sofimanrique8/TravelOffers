from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('ofertas/', views.lista_ofertas, name='lista_ofertas'),
    path('ofertas/<int:oferta_id>/', views.detalle_oferta, name='detalle_oferta'),

    path('paises/', views.lista_paises, name='lista_paises'),
    path('paises/<int:pais_id>/', views.detalle_pais, name='detalle_pais'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
]
