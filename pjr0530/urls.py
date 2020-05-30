from django.contrib import admin
from django.urls import path, include
import app0530.views
import app0530.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app0530.views.home, name="home"),
    path('app0530/', include(app0530.urls)),
]
