from django.db import models
from apps.Auditoria.models import Auditoria
from apps.Catalogos.models import Estatus
from apps.Dependencias.models import Dependencia
from datetime import datetime
# Create your models here.
class Observaciones(models.Model):
	idObservaciones = models.AutoField(primary_key=True, null=False)
	idAuditoria = models.ForeignKey(Auditoria, null=True, on_delete=models.CASCADE)
	TipoObservacion = models.CharField(max_length=100,null=False)
	FechaInicio =  models.DateField(null=True)
	TituloObservacion = models.CharField(max_length=100,null=True)
	Observacion = models.CharField(max_length=3000,null=True)
	Dependencia = models.ManyToManyField(Dependencia,null=True)
	Enlace = models.CharField(max_length=100,null=True)
	Usuario = models.CharField(max_length=100, null=False)
	Plazo = models.IntegerField(blank=True, default=0, null=False)
	# Documento = models.FileField(upload_to="archivos/", null=True, blank=True)
	# Resumen = models.FileField(upload_to="archivos/", null=True, blank=True)
	Estatus = models.ForeignKey(Estatus,null=True, default=1)
	Bloqueado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	Eliminado = models.IntegerField(blank=True, default=0, null=False, editable = False)
	FechaCreacion = models.DateField(auto_now=True, editable =False)
	FechaActualizacion = models.DateTimeField(default=datetime.now(), blank=True, editable = False)
	def __str__(self):
		return '{}'.format(self.TituloObservacion)
