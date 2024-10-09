from django.db import models
from usuarioPadreFamilia.models import UsuarioPadreFamilia

# Create your models here.
class Cronograma(models.Model):
    id_cronograma = models.IntegerField(default=0)
    mes = models.CharField(max_length=20)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado_pago = models.CharField(max_length=20, default='PENDIENTE')
    usuario_padre = models.ForeignKey(UsuarioPadreFamilia, on_delete=models.CASCADE, default=1)  # Cambia 1 por un ID válido
    
    def __str__(self):
        return f"{self.mes} - {self.estado_pago}"