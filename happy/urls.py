from django.contrib import admin
from django.urls import path
from .views import Pag1,Perros,Gatos

urlpatterns = [
    path('',Pag1,name="inicio"),
    path('perros',Perros,name="Perros"),
    path('gatos',Gatos, name="Gatos"),    
]