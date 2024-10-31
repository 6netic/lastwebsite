from django.contrib import admin
from django.urls import path, include
from mainsite import views
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('mainsite/', include("mainsite.urls")),
    path('madishop/', include("madishop.urls")),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

