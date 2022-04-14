from rest_framework import serializers
from app.models import *


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Oferta
        fields = '__all__'

class LanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lance
        fields = '__all__'
