from django.db import models

class Estatus(models.Model):
	idEstatus = models.AutoField(primary_key=True, null=False)
	Estatus = models.CharField(max_length=100)
	Eliminado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	def __str__(self):
		return '{}'.format(self.Estatus)