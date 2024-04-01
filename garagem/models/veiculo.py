from django.db import models
from garagem.models.cor import Cor
from garagem.models.modelo import Modelo

class Veiculo(models.Model):
    ano = models.IntegerField()
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, null=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos", default="")

    def __str__(self):
        return f"{self.modelo} ({self.ano}) ({self.cor})"