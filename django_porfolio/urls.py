from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from porfolio import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("blog/", include("blog.urls")),
]

# para servier archivos estaticos estndo en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
