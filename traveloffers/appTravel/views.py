from django.shortcuts import render, get_object_or_404
from .models import Oferta, Pais, Categoria, Imagen

# Portada
def index(request):
    paises = Pais.objects.all()
    ofertas_por_pais = {}
    for pais in paises:
        oferta = Oferta.objects.filter(pais=pais).order_by('precio').first()
        if oferta:
            ofertas_por_pais[pais] = oferta
    return render(request, 'appTravel/index.html', {'ofertas_por_pais': ofertas_por_pais})


# Listas
def lista_ofertas(request):
    ofertas = Oferta.objects.all()
    return render(request, 'appTravel/lista_ofertas.html', {'ofertas': ofertas})

def lista_paises(request):
    paises = Pais.objects.all()
    return render(request, 'appTravel/lista_paises.html', {'paises': paises})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'appTravel/lista_categorias.html', {'categorias': categorias})


# Detalles
def detalle_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, pk=oferta_id)
    imagenes = Imagen.objects.filter(oferta=oferta).order_by('id')
    return render(request, 'appTravel/detalle_oferta.html', {
        'oferta': oferta,
        'imagenes': imagenes,
    })

def detalle_pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    ofertas = Oferta.objects.filter(pais=pais)
    return render(request, 'appTravel/detalle_pais.html', {'pais': pais, 'ofertas': ofertas})

def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    ofertas = categoria.oferta_set.all()
    return render(request, 'appTravel/detalle_categoria.html', {'categoria': categoria, 'ofertas': ofertas})
