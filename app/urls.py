
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Página inicial. acesse a rota api/")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('', home),
]

# Adicionar configuração para servir arquivos de mídia durante o desenvolvimento e produção
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
