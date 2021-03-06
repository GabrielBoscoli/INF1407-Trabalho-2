from django.db import models
from django.conf import settings

# Create your models here.

class Gasto(models.Model):
    descricao = models.CharField(max_length=100, help_text="Entre com a descrição do gasto")
    custo = models.DecimalField(help_text="Entre com o custo", decimal_places=2, max_digits=10)
    data = models.DateField(help_text="Data do gasto no formato <em>DD/MM/AAAA<em>")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return "descrição: " + self.descricao + "\ncusto: " + self.custo + "\ndata: " + self.data