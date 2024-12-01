from django.db import models
from django.utils import timezone

class Property(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    description = models.TextField()  # Adicionando campo de descrição
    bedrooms = models.IntegerField()  # Adicionando campo de quartos
    bathrooms = models.IntegerField()  # Adicionando campo de banheiros
    image = models.ImageField(upload_to='properties/', null=True, blank=True)  # Adicionando campo de imagem
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)  # Corrigido para apenas auto_now_add=True

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
