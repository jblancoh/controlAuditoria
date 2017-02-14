from django.db import models
from apps.TipoAuditoria.models import TipoAuditoria

# Create your models here.
class Auditoria(models.Model):
	idAuditoria = models.AutoField(primary_key=True, null=False)
	idTipoAuditoria = models.ForeignKey(TipoAuditoria, null=True, on_delete=models.CASCADE)
	FechaInicioAuditoria =  models.DateField(null=True)
	FechaTerminoAuditoria = models.DateField(null=True)
	NombreAuditoria = models.CharField(max_length=100)
	Eliminado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	def __str__(self):
		return '{}'.format(self.NombreAuditoria)