from principal.models import *
from principal.forms import RegisterUserCreateForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import PerfilForm

def lista_usuarios(request):
	usuarios = User.objects.all()
	return render_to_response('usuarios.html', {'usuarios':usuarios}, context_instance=RequestContext(request))

#Registrar un nuevo usuario al sistema.
def nuevo_usuario(request):
	if request.method=='POST':
		formulario = RegisterUserCreateForm(request.POST)
		#Hay diferencia entre is_valid() y is_valid, mientras que el primero valida mostrando los errores el ultimo no muestra los errores.
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = RegisterUserCreateForm()
	return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

<<<<<<< HEAD

def editar(request,id_user_modificar):
	usuario=request.user
	user_modificar = User.objects.get(pk=id_user_modificar)
	if usuario.is_superuser == 1:
		return render_to_response('editar_adm.html',{'usuario' :user_modificar}, context_instance=RequestContext(request))
	else:
		return render_to_response('editar_user.html',{'usuario' :user_modificar}, context_instance=RequestContext(request))	

=======
def editar(request,id_user):
	variable ='fd'
	if variable =='admin':
		return render_to_response('editar_adm.html', context_instance=RequestContext(request))
	usuario = User.objects.filter(pk=id_user)
	return render_to_response('editar_user.html', context_instance=RequestContext(request))	
>>>>>>> 64983ee558b09b3d3c65867bd78754b512d1ee00

def ver_usuario(request, id_usuario):	
	dato = User.objects.get(pk=id_usuario)
	dato2 = PerfilUsuario.objects.filter(usuario=id_usuario)
	return render_to_response('ver_usuario.html',{'usuario':dato,'verPerfil':dato2},context_instance = RequestContext(request))
<<<<<<< HEAD

=======
>>>>>>> 64983ee558b09b3d3c65867bd78754b512d1ee00

def nuevo_perfil(request):
	if request.method=='POST':
		formulario=PerfilForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/registrar')
	else: 
		formulario=PerfilForm()
<<<<<<< HEAD

	return render_to_response('nuevoperfil.html',{'formulario':formulario}, context_instance=RequestContext(request))

=======
	return render_to_response('nuevoperfil.html',{'formulario':formulario}, context_instance=RequestContext(request))
>>>>>>> 64983ee558b09b3d3c65867bd78754b512d1ee00
