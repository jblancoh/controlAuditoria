from django import forms
from apps.Observaciones.models import  Observaciones
#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.contrib.auth.models import User	
from django.contrib.admin.widgets import AdminDateWidget 



class ObservacionesModalForm(forms.ModelForm):

	class Meta:
		model = Observaciones

		fields = [
 		'idAuditoria',
 		'FechaInicio',

 		'TituloObservacion',
 		'Observacion',
 		'Usuario',
 		
 		#'Estatus',

 		] 
		labels = {
 		'idAuditoria': 'Auditoría',
 		'FechaInicio': 'Fecha de inicio',
 		
 		'TituloObservacion': 'Titulo de la Observacion',
 		'Observacion': 'Observación',
 		'Usuario': 'Usuario',
 		
 		#'Estatus': 'Estatus',
 		}
		widgets = {
		'idAuditoria': forms.Select(attrs={'class':'form-control','readonly':'readonly'}),
		#'FechaInicio': forms.DateField(widget=DateWidget(usel10n=True)),
		'FechaInicio': forms.DateInput(attrs={'type': 'date','class':'form-control','readonly':'readonly'}),
		'FechaTermino': forms.DateInput(attrs={'type': 'date','class':'form-control','readonly':'readonly'}),
		'TituloObservacion': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
		'Observacion': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
		'Usuario': forms.HiddenInput(),
		
		#'Estatus': forms.Select(attrs={'class':'form-control'}),
 		}

