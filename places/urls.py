from django.urls import path
from .views import HomeView, PlaceListView, PlaceDetailView, PlaceCreateView
from . import views

app_name = 'places'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('places/', PlaceListView.as_view(), name='place_list'),
    path('places/add/', PlaceCreateView.as_view(), name='place_add'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place_detail'),
    path('random/', views.random_place, name='random_place'),
]
