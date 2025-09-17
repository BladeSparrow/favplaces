<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Place
from .forms import PlaceForm
import random


class HomeView(TemplateView):
    template_name = 'places/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['top_places'] = Place.objects.all()[:3]
        return ctx


class PlaceListView(ListView):
    model = Place
    template_name = 'places/place_list.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.all()


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/place_detail.html'


class PlaceCreateView(CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/place_form.html'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('places:place_list')


from django.http import HttpResponse

def random_place(request):
    qs = Place.objects.all()
    if not qs.exists():
        html = '<div style="text-align:center;padding:2em;"><h2>Список порожній 😔</h2><p>Додайте своє перше улюблене місце!</p></div>'
        return HttpResponse(html)
    choices = list(qs)
    weights = [p.rating ** 2 for p in choices]
    picked = random.choices(choices, weights=weights, k=1)[0]
    html = render_to_string('places/_place_preview.html', {'place': picked, 'show_full_link': True})
    return HttpResponse(html)
>>>>>>> 05b0b54 (Lab implementation: models, views, templates, cleanup)
