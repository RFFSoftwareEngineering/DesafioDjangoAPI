from rest_framework import viewsets
from app import serializers
from app import models


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.Empresa.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()

class OfertaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OfertaSerializer
    queryset = models.Oferta.objects.all()

class LanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LanceSerializer
    queryset = models.Lance.objects.all()
