from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from apps.Seguimientos.forms import SeguimientosForm,AlertasForm
from apps.Seguimientos.models import  Seguimientos, TipoSeguimiento, Alerta
from django.contrib.auth.models import User	
from django.core.urlresolvers import reverse_lazy


def crear_seguimientos(request):

	if request.method == 'POST':
		form = SeguimientosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('indexSeguimientos:indexSeguimientos')
	else:
		form = SeguimientosForm()
	return render(request,'Seguimientos/seguimientos_form.html', {'form':form})

def seguimientos_edit(request, idSeguimiento):
	seguimientos = Seguimientos.objects.get(idSeguimiento=idSeguimiento)
	if request.method == 'GET':
		form = SeguimientosForm(instance=seguimientos)
	else:
		form = SeguimientosForm(request.POST, instance=seguimientos)
		if form.is_valid():
			form.save()
		return redirect('indexSeguimientos:indexSeguimientos')
	return render (request, 'Seguimientos/seguimientos_form.html', {'form':form})

def seguimientos_delete(request, idSeguimiento):
	seguimientos = Seguimientos.objects.get(idSeguimiento=idSeguimiento)
	if request.method == 'POST':
		seguimientos.delete()
		return redirect('indexSeguimientos:indexSeguimientos')
	return render (request, 'Seguimientos/seguimientos_delete.html', {'seguimientos':seguimientos})

class seguimientosList(ListView):
	model = Seguimientos
	template_name = 'Seguimientos/index.html'

class SeguimientosProcesoList(ListView):
	queryset = Seguimientos.objects.filter(Estatus=1)
	template_name = 'Seguimientos/index.html'


class SeguimientosFinalizadasList(ListView):
	queryset = Seguimientos.objects.filter(Estatus=2)
	template_name = 'Seguimientos/index.html'




def crear_alerta(request):

	if request.method == 'POST':
		form = AlertasForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('indexAlertas:indexAlertas')
	else:
		form = AlertasForm()
	return render(request,'Alertas/alertas_form.html', {'form':form})

def alertas_edit(request, idAlerta):
	alertas = Alerta.objects.get(idSeguimiento=idSeguimiento)
	if request.method == 'GET':
		form = AlertasForm(instance=alertas)
	else:
		form = AlertasForm(request.POST, instance=alertas)
		if form.is_valid():
			form.save()
		return redirect('indexAlertas:indexAlertas')
	return render (request, 'Alertas/alertas_form.html', {'form':form})

def alertas_delete(request, idSeguimiento):
	alertas = Alerta.objects.get(idSeguimiento=idSeguimiento)
	if request.method == 'POST':
		alertas.delete()
		return redirect('indexAlertas:indexAlertas')
	return render (request, 'Alertas/alertas_delete.html', {'alertas':alertas})

class alertasList(ListView):
	model = Alerta
	template_name = 'Alertas/index.html'

