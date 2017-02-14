from django import forms
from apps.Auditoria.models import  Auditoria
#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.contrib.auth.models import User	
class AuditoriaForm(forms.ModelForm):

	class Meta:
		model = Auditoria

		fields = [
 		'idAuditoria',
 		'idTipoAuditoria',
 		'FechaInicioAuditoria',
 		'FechaTerminoAuditoria',
 		'NombreAuditoria',
 	
 	

 		] 
		labels = {
 		'idAuditoria': 'idAuditoria',
 		'idTipoAuditoria': 'Tipo de auditoría:',
 		'FechaInicioAuditoria': 'Fecha de inicio de la auditoría:',
 		'FechaTerminoAuditoria': 'Fecha de termino de la auditoría:',
 		'NombreAuditoria': 'Nombre de la auditoría:',
 		
 		}
		widgets = {
		'idAuditoria': forms.Select(attrs={'class':'form-control'}),
		#'FechaInicio': forms.DateField(widget=DateWidget(usel10n=True)),
		'idTipoAuditoria': forms.Select(attrs={'class':'form-control'}),
		'FechaInicioAuditoria': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
		'FechaTerminoAuditoria': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
		'NombreAuditoria': forms.TextInput(attrs={'class':'form-control'}),
		
 		}

