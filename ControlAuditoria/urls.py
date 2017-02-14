"""ControlAuditoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Observacion/', include('apps.Observaciones.urls', namespace="indexObservacion")),
    url(r'^TipoAuditoria/', include('apps.TipoAuditoria.urls', namespace="indexTipoAuditoria")),
    url(r'^Auditoria/', include('apps.Auditoria.urls', namespace="indexAuditoria")),
    url(r'^Seguimientos/', include('apps.Seguimientos.urls', namespace="indexSeguimientos")),


    url(r'^$', login, {'template_name':'index.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': 'login'}, name='logout'),
    
    url(r'^reset/password_reset', password_reset, 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name':'registration/password_reset_email.html'}, 
        name='password_reset'),
    url(r'^password_reset_done', password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]
