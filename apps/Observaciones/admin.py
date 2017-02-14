from django.contrib import admin
from apps.Auditoria.models	import  Auditoria
from apps.Observaciones.models import Observaciones
from apps.Seguimientos.models import TipoSeguimiento, Seguimientos, Alerta
from apps.Catalogos.models import Estatus
from apps.TipoAuditoria.models import TipoAuditoria
from apps.Dependencias.models import Dependencia
admin.site.register(TipoAuditoria)
admin.site.register(Auditoria)
#admin.site.register(Observaciones)
admin.site.register(TipoSeguimiento)
admin.site.register(Seguimientos)
admin.site.register(Alerta)
admin.site.register(Estatus)
admin.site.register(Dependencia)

class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ('TituloObservacion','FechaInicio', 'FechaTermino','Observacion','Usuario','Avance','Estatus',)

admin.site.register(Observaciones)