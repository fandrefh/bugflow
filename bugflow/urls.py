"""bugflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#Para servir os css e js localmente
from django.conf import settings
from django.conf.urls.static import static

from bugflow.home import views

from bugflow.accounts import urls as accounts_urls
from bugflow.projects import urls as projects_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('projects/', include(projects_urls, namespace='projects')),
    path('api/v1/', include(projects_urls, namespace='projects_apis')),
    path('', views.home_page, name='home_page'),
]

#Para servir os css e js localmente
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
