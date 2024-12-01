from django.shortcuts import render
from .models import Property, Testimonial

# View para a página inicial (home)
def home(request):
    properties = Property.objects.all()  # Obtém todas as propriedades
    return render(request, 'properties/home.html', {'properties': properties})

# View para listar todas as propriedades
def properties(request):
    properties = Property.objects.all()  # Obtém todas as propriedades
    return render(request, 'properties/properties_list.html', {'properties': properties})

# View para listar todos os depoimentos
def testimonials(request):
    testimonials = Testimonial.objects.all()  # Obtém todos os depoimentos
    return render(request, 'properties/testimonials.html', {'testimonials': testimonials})
