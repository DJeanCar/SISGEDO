from principal.models import *
from django.contrib.auth.models import User

def datos_globales(request):
	try:
		usuario = request.user
		perfiles = PerfilUsuario.objects.filter(usuario=usuario)
		for perfil in perfiles:
			if perfil.online == 1:
				data = perfil.tipo
	except:
		data = ""
	dict = {
		'online': data,
	}
	return dict