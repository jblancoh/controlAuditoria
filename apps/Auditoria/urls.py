from django.conf.urls import url, include
from django.contrib import admin
from apps.Auditoria.views import  crear_auditoria, auditoria_edit, auditoria_delete, \
 auditoriaList
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^Auditoria$', login_required(auditoriaList.as_view()), name='indexAuditoria'),
    url(r'^NuevaAuditoria$',login_required(crear_auditoria), name='crear_auditoria'),
    url(r'^editarAuditoria/(?P<idAuditoria>\d+)/$',login_required(auditoria_edit), name='auditoria_edit'),
    url(r'^eliminarAuditoria/(?P<idAuditoria>\d+)/$', login_required(auditoria_delete), name='auditoria_delete'),


  
]