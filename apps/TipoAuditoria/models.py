from django.db import models

# Create your models here.
class TipoAuditoria(models.Model):
	idTipoAuditoria = models.AutoField(primary_key=True, null=False)
	TipoAuditoria = models.CharField(max_length=100)
	Eliminado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	def __str__(self):
		return '{}'.format(self.TipoAuditoria)