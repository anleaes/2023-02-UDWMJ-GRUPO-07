"""projetoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('accounts.urls', namespace='accounts')),
    path('adocoes/', include('adocoes.urls', namespace='adocoes')),
    path('atendimentos/', include('atendimentos.urls', namespace='atendimentos')),
    path('animais/', include('animais.urls', namespace='animais')),
    path('adotantes/', include('adotantes.urls', namespace='adotantes')),
    path('doadores/', include('doadores.urls', namespace='doadores')),
    path('ongs/', include('ongs.urls', namespace='ongs')),
    path('veterinarios/', include('veterinarios.urls', namespace='veterinarios')),
    path('', include('core.urls', namespace='core')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)