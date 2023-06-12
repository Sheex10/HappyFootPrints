from rest_framework import serializers
from happy.models import Usuario, Venta

#clase de usuario

class usuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_admin','rut','nombre','apellido','direccion','tarjetas']

#clase registro de venta

class registro_ventaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venta
        field = ['id_pedido','cantidad','precio','fecha']
