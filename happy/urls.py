from django.contrib import admin
from django.urls import path
from .views import Pag1,Perros,BañoEco,Cama,Casa,Correa,Juguete,Plato,Gatos,Alfombra,rascador,collar,CamaGatos,JugueteGato,Arenero,Carrito

urlpatterns = [
    path('',Pag1,name="inicio"),

    path('perros',Perros,name="Perros"),
    path('bañoeco',BañoEco, name="BañoEco"),
    path('cama',Cama, name="Cama"),
    path('casa',Casa, name="Casa"),
    path('correa',Correa, name="Correa"),
    path('juguete',Juguete, name="Juguete"),
    path('plato',Plato, name="Plato"),

    path('gatos',Gatos, name="Gatos"),   
    path('alfombra',Alfombra, name="Alfombra"),
    path('rascador',rascador,name="rascador"),
    path('collar',collar,name="collar"),
    path('camagatos',CamaGatos,name="CamaGatos"),
    path('juguetegato',JugueteGato,name="JugueteGato"),
    path('arenero',Arenero,name="Arenero"),

    path('carrito',Carrito,name="Carrito"),
]