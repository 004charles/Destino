from django.contrib import admin
from django.urls import path, include
from usuarios import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('rest_framework.urls')),
    path('api/', include('usuarios.urls')),
    path('', views.index, name = "index"),

]
