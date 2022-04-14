from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    doc = models.CharField(max_length=120)
    about = models.CharField(max_length=120)
    active = models.BooleanField()
    site = models.CharField(max_length=120)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    doc = models.CharField(max_length=120)
    about = models.CharField(max_length=120)
    active = models.BooleanField()
    site = models.CharField(max_length=120)

class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    id_cliente2 = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    from_place = models.CharField(max_length=120)
    initial_value = models.FloatField()
    amount = models.FloatField()
    amount_type = models.CharField(max_length=10)

class Lance(models.Model):
    id_provider = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_offer = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    value = models.FloatField()
    amount = models.FloatField()
