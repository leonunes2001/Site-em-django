from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from properties.views import home  # Importando a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Página inicial
    path('propriedades/', include('properties.urls')),  # Inclui as URLs da app 'properties'
]

# Serve arquivos de mídia no desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
