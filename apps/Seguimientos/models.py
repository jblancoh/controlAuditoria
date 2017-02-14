from django.db import models
from apps.Observaciones.models import Observaciones
from datetime import datetime
from django.contrib.auth.models import User	
from apps.Catalogos.models import Estatus
# Create your models here.
class TipoSeguimiento(models.Model):
	idTipoSeguimiento = models.AutoField(primary_key=True, null=False)
	TipoSeguimiento = models.CharField(max_length=100)
	Eliminado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	def __str__(self):
		return '{}'.format(self.TipoSeguimiento)

class Seguimientos(models.Model):
	idSeguimiento = models.AutoField(primary_key=True, null=False)
	idObservacion = models.ForeignKey(Observaciones, null=True, on_delete=models.CASCADE)
	FechaInicio =  models.DateField()
	FechaTermino =  models.DateField()
	idTipoSeguimiento = models.ForeignKey(TipoSeguimiento, null=True, on_delete=models.CASCADE)
	Oficio = models.CharField(max_length=100)
	Destinatario = models.CharField(max_length=100)
	Fechaseguimiento = models.DateTimeField(default=datetime.now(), blank=True)
	Atendio = models.CharField(max_length=100)
	Observacion = models.CharField(max_length=100)
	Usuario = models.CharField(max_length=100, null=False)
	Avance = models.CharField(max_length=100)
	Estatus = models.ForeignKey(Estatus,null=True, default=1)
	Bloqueado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	Eliminado = models.IntegerField(blank=True, default=0, null=False, editable = False)

	def __str__(self):
		return '{}'.format(self.Observacion)

class Alerta(models.Model):
	idAlerta = models.AutoField(primary_key=True, null=False)
	idSeguimiento = models.ForeignKey(Seguimientos, null=True, on_delete=models.CASCADE)
	Fecha =  models.DateField()
	Recordatorio = models.CharField(max_length=100)
	Usuario = models.CharField(max_length=100, null=False)
	Estatus = models.ForeignKey(Estatus,null=True, default=1)
	Bloqueado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	Eliminado =  models.IntegerField(blank=True, default=0, null=False, editable = False)

	def __str__(self):
		return '{}'.format(self.Recordatorio)