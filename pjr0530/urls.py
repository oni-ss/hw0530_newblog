from django.contrib import admin
from django.urls import path, include
import app0530.views
import app0530.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app0530.views.home, name="home"),
    path('app0530/', include(app0530.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
