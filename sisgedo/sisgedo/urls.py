from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'principal.views.home'),
    url(r'^usuarios/$', 'principal.views.lista_usuarios'),
	url(r'^usuarios/registrar/$', 'principal.views.registrar_usuario'),
    url(r'^usuarios/editar-usuario/(?P<id_usuario>\d+)$', 'principal.views.editar_usuario'),
    url(r'^usuarios/(?P<id_usuario>\d+)/perfiles$','principal.views.ver_perfiles'),

    #Solo se esta usando el de arriba usuarios/editar/ ..... 
    #url(r'^editar-usuario/(?P<id_usuario>\d+)$', 'principal.views.editar_usuario'),
    url(r'^ver_usuario/(?P<id_usuario>\d+)$','principal.views.ver_usuario'),
    url(r'^ver_perfiles/(?P<id_usuario>\d+)$','principal.views.ver_perfiles'),
    url(r'^nuevo_perfil/(?P<id_usuario>\d+)$','principal.views.nuevo_perfil'),

    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^privado/$','principal.views.privado'),
    url(r'^cerrar/$', 'principal.views.cerrar'),
    
    url(r'^ajax/$', 'principal.views.ajax'),
    url(r'^probandoajax/$', 'principal.views.probandoajax'),
    url(r'^edit_estado/$', 'principal.views.edit_estado'),
    
    url(r'^editar_perfil/(?P<id_perfil>\d+)$', 'principal.views.editar_perfil'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ajax-username/$', 'principal.views.ajax_username'),
)
