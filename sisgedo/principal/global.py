from principal.models import *
from django.contrib.auth.models import User

def variables_globales(request):
	data = ""
	try:
		usuario = request.user
		try:
			perfiles = PerfilUsuario.objects.filter(usuario=usuario)
			if perfiles:
				for perfil in perfiles:
					if perfil.online == True:
						data = perfil.tipo
			else:
				data = "No tiene perfiles"			
		except:
			data = "No tiene perfiles"
	except:
		data = "No estas logueado"
	dict = {
		'online': data,
	}
	return dict