from django.urls import path
from .views import Pag1,Perros,BañoEco,Cama,Casa,Correa,Juguete,Plato,Gatos,Alfombra,rascador,collar,CamaGatos,JugueteGato,Arenero,Carrito,Razas,InicioSesion,register,Editar,Editar2,EditPerfil,Clave,Clave2,administrativo,Agregar,formProductos

urlpatterns = [
    path('',Pag1,name="inicio"),
    path('InicioSesion',InicioSesion, name="IniSesion"),
    path('registro',register,name="register"),
    path('Editar',Editar,name="Editar"),
    path('Editar2',Editar2,name="Editar2"),
    path('EditPerfil',EditPerfil,name="EditPerfil"),
    path('Clave',Clave,name="Clave"),
    path('Clave2',Clave2,name="Clave2"),
    path('administrativo',administrativo,name="administrativo"),
    path('Agregar',Agregar,name="Agregar"),
    path('formProductos',formProductos, name="formProductos"),


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
    path('razas',Razas, name="Razas"),
]