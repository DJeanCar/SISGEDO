from principal.models import *
from django.contrib.auth.models import User

def datos_globales(request):
	try:
		usuario = request.user
		try:
			perfiles = PerfilUsuario.objects.filter(usuario=usuario)
			if perfiles:
				for perfil in perfiles:
					if perfil.online == 1:
						data = perfil.tipo
					else:
						data = ""
			else:
				data ="No tiene perfiles"			
		except:
			data = "No tiene perfiles"
	except:
		data = ""
	dict = {
		'online': data,
	}
	return dict