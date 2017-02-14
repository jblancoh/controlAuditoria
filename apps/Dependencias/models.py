from django.db import models

from datetime import datetime
# Create your models here.
class Dependencia(models.Model):
	idDependencia = models.AutoField(primary_key=True, null=False)
	Dependencia = models.CharField(max_length=100,null=True)
	Siglas = models.CharField(max_length=100,null=True)
	Bloqueado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	Eliminado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	def __str__(self):
		return '{}'.format(self.Dependencia)