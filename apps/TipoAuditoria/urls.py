from django.conf.urls import url, include
from django.contrib import admin
from apps.TipoAuditoria.views import crear_tipoAuditoria, tipoAuditoria_edit, tipoAuditoria_delete,  \
tipoAuditoriaList, tipoAuditoriaEliminarV
from django.contrib.auth.decorators import login_required

urlpatterns = [

   	url(r'^$', login_required(tipoAuditoriaList.as_view()), name='indexTipoAuditoria'),
  	url(r'^nuevo$',login_required(crear_tipoAuditoria), name='Crear_TipoAuditoria'),
    url(r'^editar/(?P<idTipoAuditoria>\d+)/$',login_required(tipoAuditoria_edit), name='Editar_TipoAuditoria'),
  	url(r'^eliminar/(?P<pk>\d+)/$', login_required(tipoAuditoriaEliminarV.as_view()), name='Eliminar_TipoAuditoria'),

  
]