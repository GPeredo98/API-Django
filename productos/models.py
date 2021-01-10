from datetime import datetime

from django.db import models


class Producto(models.Model):

    class ProductoCategorias(models.IntegerChoices):
        MODA = 1
        DEPORTE = 2
        SALUD = 3
        BELLEZA = 4
        HERRAMIENTAS = 5
        TECNOLOGIA = 6

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    categoria = models.IntegerField(choices=ProductoCategorias.choices, default=ProductoCategorias.MODA)
    precio = models.IntegerField(null=False)
    cantidad = models.IntegerField(null=False)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.now())
    imagen = models.TextField(null=True)

    class Meta:
        db_table = 'productos'