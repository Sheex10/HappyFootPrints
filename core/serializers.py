from rest_framework import serializers
from happy.models import Usuario, Venta

#clase de usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_admin','rut','nombre','apellido','direccion','tarjetas']



