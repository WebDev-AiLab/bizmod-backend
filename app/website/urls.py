from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('constructor/', include('constructor.urls', namespace='constructor')),
    path('', include('index.urls', namespace='index'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
