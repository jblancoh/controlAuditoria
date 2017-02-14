from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from apps.Observaciones.forms_observacion import ObservacionesForm
from apps.Observaciones.forms_modal import ObservacionesModalForm
from apps.Observaciones.models import  Observaciones
from django.contrib.auth.models import User	
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.template import Context, Template
from django.conf import settings
# Checar el from django.views.generic import DetailView

class ObservacionDetallesview(DetailView):
    model = Observaciones
	#queryset = Observaciones.objects.get(idObservaciones=idObservaciones)
	#template_name = 'Observaciones/observacion_form.html'

def crear_observacion(request):	
	aceptar = False
	if request.method == 'POST':
		form = ObservacionesForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			#def Upload(request):
				#for count, x in enumerate(request.FILES.getlist(form.Documento)):
				#	def process(f):
				#		with open('/Users/ServerVostro/Documents/Desarrollo_Python/ObservacionAuditoria/media/archivos', 'wb+') as destination:        			
        		#				for c in request.FILES['Documento'].chunks(): 
            	#						destination.write(chunk)
        		#				process(x)
		return redirect('indexObservacion:indexObservacion')
		#return HttpResponse("Files(s) uploaded!")
	else:
		form = ObservacionesForm()
	return render(request,'Observaciones/observacion_form.html',  {'form':form})


def observacion_edit(request, idObservaciones):
	Observacion = Observaciones.objects.get(idObservaciones=idObservaciones)
	if request.method == 'GET':
		form = ObservacionesForm(instance=Observacion)
	else:
		form = ObservacionesForm(request.POST, instance=Observacion)
		if form.is_valid():
			form.save()
		return redirect('indexObservacion:indexObservacion')
	return render (request, 'Observaciones/observacion_form.html', {'form':form})


def observacion_modal(request, idObservaciones):
	Observacion = Observaciones.objects.get(idObservaciones=idObservaciones)
	
	if request.method == 'GET':
		form = ObservacionesModalForm(instance=Observacion)
	else:
		
		form = ObservacionesModalForm(request.POST, instance=Observacion)
	return render (request, 'Observaciones/observacion_modal.html', {'form':form})


def finalizarobservacion_edit(request, idObservaciones):
	Observacion = Observaciones.objects.get(idObservaciones=idObservaciones)
	Observacion = Observaciones(idObservaciones=idObservaciones, FechaInicio=Observacion.FechaInicio, FechaTermino=Observacion.FechaTermino,TituloObservacion=Observacion.TituloObservacion,Observacion=Observacion.Observacion, Usuario=Observacion.Usuario,Avance=Observacion.Avance, Estatus_id=2, Bloqueado=1, idAuditoria_id=Observacion.idAuditoria_id)
	
	if request.method == 'GET':
		Observacion.save()
	return redirect('indexObservacion:indexObservacion')
	

def observacion_delete(request, idObservaciones):
	observacion = Observaciones.objects.get(idObservaciones=idObservaciones)
	if request.method == 'POST':
		observacion.delete()
		return redirect('indexObservacion:indexObservacion')
	return render (request, 'Observaciones/observacion_delete.html', {'Observacion':observacion})

class observacionProcesoList(ListView):
	queryset = Observaciones.objects.filter(Estatus=1)
	template_name = 'Observaciones/index.html'


class observacionFinalizadasList(ListView):
	queryset = Observaciones.objects.filter(Estatus=2)
	template_name = 'Observaciones/index.html'

class ObservacionList(ListView):
	model = Observaciones
	template_name =  'Observaciones/index.html'