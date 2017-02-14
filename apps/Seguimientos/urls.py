from django.conf.urls import url, include
from django.contrib import admin
from apps.Seguimientos.views import  crear_seguimientos, seguimientos_edit, seguimientos_delete, \
 seguimientosList,SeguimientosFinalizadasList
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^Seguimientos$', login_required(seguimientosList.as_view()), name='indexSeguimientos'),
    url(r'^SeguimientosFinalizados$', login_required(SeguimientosFinalizadasList.as_view()), name='indexSeguimientosFinalizados'),
    url(r'^NuevoSeguimientos$',login_required(crear_seguimientos), name='crear_seguimientos'),
    url(r'^editarSeguimientos/(?P<idSeguimiento>\d+)/$',login_required(seguimientos_edit), name='seguimientos_edit'),
    url(r'^eliminarSeguimientos/(?P<idSeguimiento>\d+)/$', login_required(seguimientos_delete), name='seguimientos_delete'),
  
]