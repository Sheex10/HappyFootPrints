from django.contrib import admin
from django.urls import path
from .views import Pag1,Perros,Gatos,Alfombra,BañoEco,rascador,collar

urlpatterns = [
    path('',Pag1,name="inicio"),
    path('perros',Perros,name="Perros"),
    path('gatos',Gatos, name="Gatos"),   
    path('alfombra',Alfombra, name="Alfombra"),
    path('bañoeco',BañoEco, name="BañoEco"),
    path('rascador',rascador,name="rascador"),
    path('collar',collar,name="collar"),
]