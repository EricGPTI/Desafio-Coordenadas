from django.urls import path
from .views import start, atual


urlpatterns = [
    path('coordenadas/start/', start, name='start'),
    path('coordenadas/atual/', atual, name='atual'),
]
