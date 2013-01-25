from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^registrar/$', 'principal.views.nuevo_usuario'),
	url(r'^editar/(?P<id_user>[-\w]+)/$', 'principal.views.editar'),
	url(r'^perfil_nuevo/$', 'principal.views.nuevo_perfil'),
	url(r'^usuarios/$', 'principal.views.lista_usuarios'),
<<<<<<< HEAD
=======
    url(r'^ver_usuario/(?P<id_usuario>\d+)$','principal.views.ver_usuario'),
	
>>>>>>> 859ca2269c2b8bbf8a7f2c3d71ab1dc85bea228f
    # Examples:
    # url(r'^$', 'sisgedo.views.home', name='home'),
    # url(r'^sisgedo/', include('sisgedo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
