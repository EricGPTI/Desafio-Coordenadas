from django.urls import path
from .views import start, atual, movement


urlpatterns = [
    path('coordenadas/start/', start, name='start'),
    path('coordenadas/atual/', atual, name='atual'),
    path('coordenadas/movement/', movement, name='movement'),
]
