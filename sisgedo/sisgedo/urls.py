from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^registrar/$', 'principal.views.nuevo_usuario'),
	url(r'^usuarios/$', 'principal.views.lista_usuarios'),
    url(r'^ver_usuario/(?P<id_usuario>\d+)$','principal.views.ver_usuario'),
    url(r'^ver_perfiles/(?P<id_usuario>\d+)$','principal.views.ver_perfiles'),
    url(r'^nuevo_perfil/(.+)$','principal.views.nuevo_perfil'),
    #url(r'^editar_perfil/(.+)$','principal.views.editar_perfil'),
	url(r'^editar/(?P<id_user_modificar>\d+)/$', 'principal.views.editar'),
    url(r'^perfil/editar/$', 'principal.views.editar_post'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
