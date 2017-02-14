from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from apps.Auditoria.forms import AuditoriaForm
from apps.Auditoria.models import  Auditoria
from django.contrib.auth.models import User	
from django.core.urlresolvers import reverse_lazy


def crear_auditoria(request):

	if request.method == 'POST':
		
		form = AuditoriaForm(request.POST)
		if form.is_valid():
			
			form.save()
		return redirect('indexAuditoria:indexAuditoria')
	else:
		form = AuditoriaForm()

	return render(request,'Auditoria/auditoria_form.html', {'form':form})

def auditoria_edit(request, idAuditoria):
	auditoria = Auditoria.objects.get(idAuditoria=idAuditoria)
	if request.method == 'GET':
		form = AuditoriaForm(instance=auditoria)
	else:
		form = AuditoriaForm(request.POST, instance=auditoria)
		if form.is_valid():
			form.save()
		return redirect('indexAuditoria:indexAuditoria')
	return render (request, 'Auditoria/auditoria_form.html', {'form':form})

def auditoria_delete(request, idAuditoria):
	auditoria = Auditoria.objects.get(idAuditoria=idAuditoria)
	if request.method == 'POST':
		auditoria.delete()
		return redirect('indexAuditoria:indexAuditoria')
	return render (request, 'Auditoria/auditoria_delete.html', {'auditoria':auditoria})

class auditoriaList(ListView):
	model = Auditoria
	template_name = 'Auditoria/index.html'

