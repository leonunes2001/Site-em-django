from django.contrib import admin
from .models import Property, Testimonial, ContactMessage

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'created_at', 'updated_at')  # Corrigido para o campo 'location'
    readonly_fields = ('created_at', 'updated_at')  # Campos que não devem ser editados

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'date_created')  # Exibindo campos corretos

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_created')  # Exibindo campos corretos

admin.site.register(Property, PropertyAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
