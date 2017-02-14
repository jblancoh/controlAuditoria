from django import forms
from apps.Observaciones.models import  Observaciones
#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget



class ObservacionesForm(forms.ModelForm):

	class Meta:
		OPTIONS = (
            ("1", "Financieras"),
            ("2", "Control internas"),
        )
		model = Observaciones

		fields = [
 		'idAuditoria',
 		'TipoObservacion',
 		'Dependencia',
 		'Enlace',
 		'FechaInicio',
 		'TituloObservacion',
 		'Observacion',
 		'Plazo',
 	# 	'Documento',
 	# 	'Resumen',
 		'Usuario',

 		#'Estatus',

 		]
		labels = {
 		'idAuditoria': 'Auditoría:',
 		'TipoObservacion': 'Tipo de observación:',
 		'Dependencia': 'Dependencia',
 		'Enlace': 'Enlace',
 		'FechaInicio': 'Fecha de inicio:',
 		'TituloObservacion': 'Titulo de la Observacion:',
 		'Observacion': 'Observación:',
 		'Plazo': 'Plazo:',
 	# 	'Documento': 'Documentación soporte',
 	# 	'Resumen': 'Resumen de observaciones',
 		'Usuario': 'Usuario:',

 		#'Estatus': 'Estatus',
 		}
		widgets = {
		'idAuditoria': forms.Select(attrs={'class':'form-control'}),
		'TipoObservacion': forms.Select(attrs={'class':'form-control'}, choices=OPTIONS),
		'Dependencia': forms.CheckboxSelectMultiple(),
		'Enlace': forms.TextInput(attrs={'class':'form-control'}),
		#'FechaInicio': forms.DateField(widget=DateWidget(usel10n=True)),
		'FechaInicio': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
		'TituloObservacion': forms.TextInput(attrs={'class':'form-control'}),
		'Observacion': forms.Textarea (attrs={'class':'form-control'}),
		'Plazo': forms.TextInput(attrs={'class':'form-control'}),
		# 'Documento': forms.ClearableFileInput(attrs={'multiple': True}),
		# 'Resumen': forms.ClearableFileInput(attrs={'multiple': True}),
		'Usuario': forms.HiddenInput(),

		#'Estatus': forms.Select(attrs={'class':'form-control'}),
 		}
