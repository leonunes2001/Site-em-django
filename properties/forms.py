from django import forms
from .models import Property, ContactMessage

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms', 'image', 'video', 'tipo', 'estado', 'comentarios']

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
