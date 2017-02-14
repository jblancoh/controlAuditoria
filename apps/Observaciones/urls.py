from django.conf.urls import url, include
from django.contrib import admin
from apps.Observaciones.views import  crear_observacion, observacion_edit, observacion_delete,finalizarobservacion_edit,observacion_modal, \
 observacionProcesoList, observacionFinalizadasList, ObservacionList,ObservacionDetallesview
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

   	#url(r'^$', login_required(tipoAuditoriaList.as_view()), name='indexTipoAuditoria'),
  	#url(r'^nuevo$',login_required(crear_tipoAuditoria), name='Crear_TipoAuditoria'),
  #  url(r'^editar/(?P<idTipoAuditoria>\d+)/$',login_required(tipoAuditoria_edit), name='Editar_TipoAuditoria'),
  #  url(r'^eliminar/(?P<pk>\d+)/$', login_required(tipoAuditoriaEliminarV.as_view()), name='Eliminar_TipoAuditoria'),
    url(r'^ObservacionesCompletas$', login_required(ObservacionList.as_view()), name='indexObservacionCompletas'),
    url(r'^Observaciones$', login_required(observacionProcesoList.as_view()), name='indexObservacion'),
    url(r'^ObservacionesFinalizadas$', login_required(observacionFinalizadasList.as_view()), name='indexObservacionFinalizadas'),
    url(r'^NuevaObservacion$',login_required(crear_observacion), name='Crear_Observacion'),
    url(r'^finalizarObservacion/(?P<idObservaciones>\d+)/$',login_required(finalizarobservacion_edit), name='Finalizar_Observacion'),
    url(r'^editarObservacion/(?P<idObservaciones>\d+)/$',login_required(observacion_edit), name='Editar_Observacion'),
    url(r'^(?P<idObservaciones>\d+)$',login_required(observacion_modal), name='Modal_Observacion'),
    url(r'^eliminarObservacion/(?P<idObservaciones>\d+)/$', login_required(observacion_delete), name='Eliminar_Observacion'),
    url(r'^(?P<slug>[-_\w]+)/$', ObservacionDetallesview.as_view(), name='Observacione_Detalles'),
    #url(r'^media/(?P<path>,*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
   # url(r'^media/(?P<path>.*)$','django.views.static.serve',{'documen_root':settings.MEDIA_ROOT}),
   # url(r'^download/(?P<path>.*)$', serve, {'document root': settings.MEDIA_ROOT}),
    
]

#urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
# UNDERNEATH your urlpatterns definition, add the following two lines:

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
