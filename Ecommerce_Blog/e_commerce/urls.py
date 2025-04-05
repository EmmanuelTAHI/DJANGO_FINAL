from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Gestion des fichiers médias en mode debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
