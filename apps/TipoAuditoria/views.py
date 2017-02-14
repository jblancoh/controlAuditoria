from django.shortcuts import render, redirect
from apps.TipoAuditoria.models import  TipoAuditoria
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView,DeleteView
from apps.TipoAuditoria.forms import TipoAuditoriaForm

# Create your views here.
def crear_tipoAuditoria(request):
	if request.method == 'POST':
		form = TipoAuditoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('indexTipoAuditoria:indexTipoAuditoria')
	else:
		form = TipoAuditoriaForm()
	return render(request,'TipoAuditoria/tipoauditoria_form.html', {'form':form})

def tipoAuditoria_edit(request, idTipoAuditoria):
	tipoauditoria = TipoAuditoria.objects.get(idTipoAuditoria=idTipoAuditoria)
	if request.method == 'GET':
		form = TipoAuditoriaForm(instance=tipoauditoria)
	else:
		form = TipoAuditoriaForm(request.POST, instance=tipoauditoria)
		if form.is_valid():
			form.save()
		return redirect('indexTipoAuditoria:indexTipoAuditoria')
	return render (request, 'TipoAuditoria/tipoauditoria_form.html', {'form':form})

def tipoAuditoria_delete(request, idTipoAuditoria):
	tipoauditoria = TipoAuditoria.objects.get(idTipoAuditoria=idTipoAuditoria)
	if request.method == 'POST':
		tipoauditoria.delete()
		return redirect('indexTipoAuditoria:indexTipoAuditoria')
	return render(request, 'TipoAuditoria/tipo_auditoria_delete.html', {'TipoAuditoria':tipoauditoria})

class tipoAuditoriaList(ListView):
	model = TipoAuditoria
	template_name = 'TipoAuditoria/index.html'

class tipoAuditoriaEliminarV(DeleteView):
	model = TipoAuditoria
	template_name = 'TipoAuditoria/tipo_auditoria_delete.html'
	success_url = reverse_lazy('indexTipoAuditoria:indexTipoAuditoria')
	