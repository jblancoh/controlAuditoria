from django import forms
from apps.Seguimientos.models import  Seguimientos,Alerta
#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.contrib.auth.models import User	
class SeguimientosForm(forms.ModelForm):

	class Meta:
		model = Seguimientos

		fields = [
 		'idSeguimiento',
 		'idObservacion',
 		'FechaInicio',
 		'FechaTermino',
 		'idTipoSeguimiento',
 		'Oficio',
 		'Destinatario',
		'Fechaseguimiento',
 		'Atendio',
 		'Observacion',
 		'Usuario',
 		'Avance',
 		] 
		labels = {
 		'idSeguimiento': 'idSeguimiento',
 		'idObservacion': 'Observación:',
 		'FechaInicio': 'Fecha de inicio del seguimiento:',
 		'FechaTermino': 'Fecha de termino del seguimiento:',
 		'idTipoSeguimiento': 'Tipo de seguimiento:',
 		'Oficio': 'Oficio:',
 		'Destinatario': 'Destinatario:',
 		'Fechaseguimiento': 'Fecha del seguimiento:',
 		'Atendio': 'Atendió:',
 		'Observacion': 'Observación:',
 		'Usuario': 'Usuario:',
 		'Avance': 'Avance:',
 		}
		widgets = {
		'idSeguimiento': forms.Select(attrs={'class':'form-control'}),
		#'FechaInicio': forms.DateField(widget=DateWidget(usel10n=True)),
		'idObservacion': forms.Select(attrs={'class':'form-control'}),
		'FechaInicio': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
		'FechaTermino': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
		'idTipoSeguimiento': forms.Select(attrs={'class':'form-control'}),
		'Oficio': forms.TextInput(attrs={'class':'form-control'}),
		'Destinatario': forms.TextInput(attrs={'class':'form-control'}),
		'Fechaseguimiento': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
		'Atendio': forms.TextInput(attrs={'class':'form-control'}),
		'Observacion': forms.TextInput(attrs={'class':'form-control'}),
		'Usuario': forms.HiddenInput(),
		'Avance': forms.TextInput(attrs={'class':'form-control'}),
 		}

class AlertasForm(forms.ModelForm):

	class Meta:
		model = Alerta

		fields = [
 		'idAlerta',
 		'idSeguimiento',
 		'Fecha',
 		'Recordatorio',
 		'Usuario',
 		
 		] 
		labels = {
 		'idAlerta': 'idAlerta',
 		'idSeguimiento': 'idSeguimiento',
 		'Fecha': 'Fecha',
 		'Recordatorio': 'Recordatorio',
 		'Usuario': 'Usuario',
 		
 		}
		widgets = {
		'idAlerta': forms.Select(attrs={'class':'form-control'}),
		#'FechaInicio': forms.DateField(widget=DateWidget(usel10n=True)),
		'idSeguimiento': forms.Select(attrs={'class':'form-control'}),
		'Fecha': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
		'Recordatorio': forms.TextInput(attrs={'class':'form-control'}),
		'Usuario': forms.HiddenInput(),
		
 		}
