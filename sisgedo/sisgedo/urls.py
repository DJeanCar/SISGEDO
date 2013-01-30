from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^usuarios/$', 'principal.views.lista_usuarios'),
	url(r'^registrar/usuario/$', 'principal.views.registrar_usuario'),

    url(r'^editar-usuario/(?P<id_usuario>\d+)$', 'principal.views.editar_usuario'),
    url(r'^ver_usuario/(?P<id_usuario>\d+)$','principal.views.ver_usuario'),
    url(r'^ver_perfiles/(?P<id_usuario>\d+)$','principal.views.ver_perfiles'),
    url(r'^nuevo_perfil/(?P<id_usuario>\d+)$','principal.views.nuevo_perfil'),

    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^privado/$','principal.views.privado'),
    url(r'^cerrar/$', 'principal.views.cerrar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
