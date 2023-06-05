from rest_framework import serializers
from happy.models import usuario, registro_venta

#clase de usuario

class usuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['id_admin','rut','nombre','apellido','direccion','tarjetas']

#clase registro de venta

class registro_ventaSerializers(serializers.ModelSerializer):
    class Meta:
        model = registro_venta
        field = ['id_pedido','cantidad','precio','fecha']
