from django import forms
from apps.TipoAuditoria.models import TipoAuditoria

class TipoAuditoriaForm(forms.ModelForm):
 	class Meta:
 		model = TipoAuditoria

 		fields = [
 		'idTipoAuditoria',
 		'TipoAuditoria',

 		] 
 		labels = {
 		'idTipoAuditoria': 'idTipoAuditoria',
 		'TipoAuditoria': 'TipoAuditoria',
 	
 		}
 		widgets = {
 		'idTipoAuditoria': forms.Select(attrs={'class':'form-control'}),
 		'TipoAuditoria': forms.TextInput(attrs={'class':'form-control'}),
 		
 		}


