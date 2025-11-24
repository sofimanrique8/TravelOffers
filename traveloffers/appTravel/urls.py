from django.urls import path
from .views import (
    IndexView,
    OfertaListView,
    OfertaDetailView,
    PaisListView,
    PaisDetailView,
    CategoriaListView,
    CategoriaDetailView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('ofertas/', OfertaListView.as_view(), name='lista_ofertas'),
    path('ofertas/<int:oferta_id>/', OfertaDetailView.as_view(), name='detalle_oferta'),

    path('paises/', PaisListView.as_view(), name='lista_paises'),
    path('paises/<int:pais_id>/', PaisDetailView.as_view(), name='detalle_pais'),

    path('categorias/', CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/<int:categoria_id>/', CategoriaDetailView.as_view(), name='detalle_categoria'),
]
