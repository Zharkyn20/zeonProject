"""zeonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.api_urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.api_urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from zeonProject import settings
# apps' urls
from apps.products import urls as p_urls
from apps.categories import urls as c_urls


# getting lists of urls
routeLists = (
    p_urls.routeList,
    c_urls.routeList,
)
# Registering all urls from apps
router = routers.DefaultRouter()
for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1], basename=route[0])


urlpatterns = [

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include(router.urls)), # Api Root

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

