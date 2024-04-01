from django.db import models
from garagem.models.marca import Marca
from garagem.models.categoria import Categoria

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelos")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="marcas")

    def __str__(self):
        return f"{self.nome} ({self.marca}) ({self.categoria})"
    