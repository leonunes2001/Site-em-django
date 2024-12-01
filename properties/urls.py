from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('propriedades/', views.properties, name='properties'),  # Página de propriedades
    path('testimonials/', views.testimonials, name='testimonials'),  # Página de depoimentos
]
