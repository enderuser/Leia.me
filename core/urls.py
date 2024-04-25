from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('usuarios.urls')),
    path('divulgar/', include('divulgar.urls')),
]
