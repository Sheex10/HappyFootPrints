from django.db import models

# Create your models here.


class Usuario(models.model):
    id_usuario =models.IntegerField(primary_key=True, verbose_name="id del usuario")
    nombre=models.CharField(max_length=20, verbose_name="nombre del usuario")
    apellido=models.CharField(max_length=20, verbose_name="apellido usuario")
    correo=models.CharField(max_length=30, verbose_name="correo usuario")
    clave=models.CharField(max_length=12, verbose_name="clave usuario")
    telefono=models.IntegerField(verbose_name="telefono usuario")
    id_rol =models.IntegerField(foreignkey=True, verbose_name="id del rol")

    def __str__(self):
        return self.Usuario
#--------------------------------------
class Registro_venta(models.model):
    id_venta =models.IntegerField(primary_key=True, verbose_name="id de venta")
    r_envio=models.CharField(max_length=100, verbose_name="registro del envio")
    costo_envio=models.IntegerField(verbose_name="costo envío")
    id_usuario =models.IntegerField(foreignkey=True, verbose_name="id del usuarioo")

    def __str__(self):
        return self.Registro_venta
#--------------------------------------
class Producto(models.model):
    id_producto =models.IntegerField(primary_key=True, verbose_name="id del producto")
    nombre=models.CharField(max_length=30, verbose_name="nombre del producto")
    descripcion=models.CharField(max_length=100, verbose_name="descripcion producto")
    precio=models.IntegerField(verbose_name="precio producto")
    foto=models.ImageField(upload_to="foto producto")
    id_categoria =models.IntegerField(foreignkey=True, verbose_name="id de categoria")

    def __str__(self):
        return self.Producto
#-------------------------------------
class Direccion(models.model):
    id_direccion =models.IntegerField(primary_key=True, verbose_name="id de direccion")
    calle=models.CharField(max_length=50, verbose_name="nombre calle")
    numero=models.IntegerField(verbose_name="numero casa")
    descripcion=models.CharField(max_length=100, verbose_name="descripcion direccion")
    id_comuna =models.IntegerField(foreignkey=True, verbose_name="id de la comuna")
    id_usuario=models.IntegerField(foreignkey=True, verbose_name="id del usuario")
    
    def __str__(self):
        return self.Direccion
#-------------------------------------
class Comuna(models.model):
    id_comuna =models.IntegerField(primary_key=True, verbose_name="id de comuna")
    nombre=models.CharField(max_length=20, verbose_name="nombre comuna")
    despacho=models.CharField(max_length=50, verbose_name="desc despacho")
    id_region=models.IntegerField(foreignkey=True, verbose_name="id de region")
    
    def __str__(self):
        return self.Comuna
#------------------------------------    
class Detalle(models.model):
    id_detalle =models.IntegerField(primary_key=True, verbose_name="id de detalle")
    cantidad=models.IntegerField(verbose_name="cantidad")
    id_venta=models.IntegerField(foreignkey=True, verbose_name="id de venta")
    id_producto=models.IntegerField(foreignkey=True, verbose_name="id de producto")
    
    def __str__(self):
        return self.Detalle
#-----------------------------------
class Rol(models.model):
    id_rol=models.IntegerField(primary_key=True, verbose_name="id de rol")
    nombre=models.CharField(max_length=30, verbose_name="nombre del rol")
    
    def __str__(self):
        return self.Rol
#-----------------------------------
class Region(models.model):
    id_region=models.IntegerField(primary_key=True, verbose_name="id de region")
    nombre=models.CharField(max_length=30, verbose_name="nombre de region")
    
    def __str__(self):
        return self.Region
#----------------------------------
class Categoria(models.model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name="id de rol")
    nombre=models.CharField(max_length=30, verbose_name="nombre de categoria")
    
    def __str__(self):
        return self.Categoria
    
#Modelos finalizados.
# :D
