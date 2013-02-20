from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'principal.views.home'),
    url(r'^usuarios/$', 'principal.views.usuarios'),
	url(r'^usuarios/registrar/$', 'principal.views.registrar_usuario'),
    url(r'^usuarios/editar/(?P<id_usuario>\d+)$', 'principal.views.editar_usuario'),
    url(r'^usuarios/(?P<id_usuario>\d+)/perfiles/$','principal.views.ver_perfiles'),

    url(r'^ajax_ver_usuario/$','principal.views.ajax_ver_usuario'),
    url(r'^nuevo_perfil/(?P<id_usuario>\d+)$','principal.views.nuevo_perfil'),

    url(r'^cerrar/$', 'principal.views.cerrar'),
    
    url(r'^editar_perfil/(?P<id_perfil>\d+)$', 'principal.views.editar_perfil'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ajax-username/$', 'principal.views.ajax_username'),
    url(r'^edit_estado/$', 'principal.views.edit_estado'),
<<<<<<< HEAD
    url(r'^edit_tipo/$', 'principal.views.edit_tipo'),
    url(r'^edit_fecha_cad/$', 'principal.views.edit_fecha_cad'),
=======
    url(r'^ajax/cambiar-online/$', 'principal.views.cambiar_online'),
    url(r'^resetear_clave/$', 'principal.views.resetear_clave'),
>>>>>>> 6bcd880d2514a04a7472eaa972d4bf292b84bb86
    
)
