from django.contrib import admin
from django.urls import path,include
from .views import lista_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listaUsuario/',lista_usuario,name="lista_usuario"),
    
]
