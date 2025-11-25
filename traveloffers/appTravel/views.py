from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .forms import ReservaInquiryForm
from .models import Oferta, Pais, Categoria, ReservaInquiry


# Portada
class IndexView(TemplateView):
    template_name = 'appTravel/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paises = Pais.objects.all()
        ofertas_por_pais = {}
        for pais in paises:
            oferta = Oferta.objects.filter(pais=pais).order_by('precio').first()
            if oferta:
                ofertas_por_pais[pais] = oferta
        context['ofertas_por_pais'] = ofertas_por_pais
        return context


# Listas
class OfertaListView(ListView):
    model = Oferta
    template_name = 'appTravel/lista_ofertas.html'
    context_object_name = 'ofertas'


class PaisListView(ListView):
    model = Pais
    template_name = 'appTravel/lista_paises.html'
    context_object_name = 'paises'


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'appTravel/lista_categorias.html'
    context_object_name = 'categorias'


# Detalles
class OfertaDetailView(DetailView):
    model = Oferta
    template_name = 'appTravel/detalle_oferta.html'
    context_object_name = 'oferta'
    pk_url_kwarg = 'oferta_id'   


class PaisDetailView(DetailView):
    model = Pais
    template_name = 'appTravel/detalle_pais.html'
    context_object_name = 'pais'
    pk_url_kwarg = 'pais_id'     

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ofertas'] = Oferta.objects.filter(pais=self.object)
        return context


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'appTravel/detalle_categoria.html'
    context_object_name = 'categoria'
    pk_url_kwarg = 'categoria_id' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ofertas'] = self.object.oferta_set.all()
        return context

class ReservaCreateView(CreateView):
    model = ReservaInquiry
    form_class = ReservaInquiryForm
    template_name = 'appTravel/reserva_form.html'
    pk_url_kwarg = 'oferta_id'

    def get_success_url(self):
        return reverse_lazy('detalle_oferta', kwargs={'oferta_id': self.object.oferta.id})

    def form_valid(self, form):
        oferta = get_object_or_404(Oferta, pk=self.kwargs['oferta_id'])
        form.instance.oferta = oferta

        response = super().form_valid(form)

        self.request.session['success_message'] = '¡Tu solicitud de reserva ha sido enviada con éxito! Te contactaremos pronto.'
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['oferta'] = get_object_or_404(Oferta, pk=self.kwargs['oferta_id'])
        return context