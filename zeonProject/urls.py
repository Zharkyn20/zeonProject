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
from django.urls import path, include, re_path
from rest_framework import routers
from zeonProject import settings
# apps' urls
from apps.products import urls as p_urls
from apps.categories import urls as c_urls
from apps.cart import urls as cart_urls
from apps.about_us import urls as about_us_urls
from apps.news import urls as news_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# getting lists of urls
routeLists = (
    p_urls.routeList,
    c_urls.routeList,
    cart_urls.routeList,
    about_us_urls.routeList,
    news_urls.routeList,
)
# Registering all urls from apps
router = routers.DefaultRouter()
for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1], basename=route[0])


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include(router.urls)), # Api Root

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
