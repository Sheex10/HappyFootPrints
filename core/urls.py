from django.urls import path,include
from .views import lista_usuario

urlpatterns = [
    path('listaUsuario/',lista_usuario,name="lista_usuario"),
    
]
