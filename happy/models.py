from django.db import models

# Create your models here.

#modelos para cada categoria HappyFootPrints

class empleado(models.Model):
    rut =models.IntegerField(primary_key=True, verbose_name="id de empleado")
    nombre = models.CharField(max_length=30, verbose_name="nombre empleado")
    apellidos = models.CharField(max_length=30, verbose_name="apellido empleado")
    direccion = models.CharField(max_length=30, verbose_name="direccion empleado")

    def __str__(self):
        return self.empleado
    
class registro_venta(models.Model):
    id_pedido =models.IntegerField(primary_key=True, verbose_name="id de pedido")
    cantidad = models.IntegerField(verbose_name="cantidad de producto")
    precio = models.IntegerField(verbose_name="precio de producto")
    fecha = models.DateField(verbose_name="fecha de registro")

    def __str__(self):
        return self.registro_venta
    
class seguridad(models.Model):
    clave = models.CharField(max_length=12, verbose_name="clave de usuario")
    correo = models.CharField(primary_key=True,max_length=30, verbose_name="correo del usuario")
    correo_respaldo = models.CharField(max_length=30, verbose_name="correo de respaldo del usuario")

    def __str__(self):
        return self.seguridad
    
class administrador(models.Model):
    id_admin =models.IntegerField(primary_key=True, verbose_name="id de admin")
    rut = models.IntegerField(verbose_name="rut del admin")
    nombre = models.CharField(verbose_name="nombre del admin")
    apellido = models.CharField(verbose_name="apellido del admin")
    direccion = models.CharField(max_length=50, verbose_name="direccion del admin")

    def __str__(self):
        return self.administrador
    
class usuario(models.Model):
    id_admin =models.IntegerField(primary_key=True, verbose_name="id de usuario")
    rut = models.IntegerField(verbose_name="rut del usuario")
    nombre = models.CharField(verbose_name="nombre del usuario")
    apellido = models.CharField(verbose_name="apellido del usuario")
    direccion = models.CharField(max_length=50, verbose_name="direccion del usuario")
    tarjetas = models.CharField(max_length=50,verbose_name="tarjetas del usuario")

    def __str__(self):
        return self.ususario
    
class producto(models.Model):
    id_producto =models.IntegerField(primary_key=True, verbose_name="id del producto")
    descripcion = models.CharField(max_length=150, verbose_name="descripcion del producto")
    peso = models.IntegerField(verbose_name="peso del producto")
    precio = models.IntegerField(verbose_name="precio del producto")

    def __str__(self):
        return self.producto
    
class happyfootprint(models.Model):
    nombre = models.CharField(verbose_name="nombre de la empresa")
    descripcion = models.CharField(max_length=150, verbose_name="descripción de la empresa")
    
    def __str__(self):
        return self.happyfootprint
    
#modelos finalizados