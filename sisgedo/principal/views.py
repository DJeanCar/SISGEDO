from principal.models import *
from principal.forms import RegisterUserCreateForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import PerfilForm, EditarUserForm, EditarPerfilForm
import json
from principal.forms import PerfilForm, EditarUserForm, EditarPerfilForm, EditarEstado

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def lista_usuarios(request):
	usuarios = User.objects.all()
	return render_to_response('usuarios.html', {'usuarios':usuarios}, context_instance=RequestContext(request))

def registrar_usuario(request):
	if request.method=='POST':
		formulario = RegisterUserCreateForm(request.POST)
		#Hay diferencia entre is_valid() y is_valid, mientras que el primero valida mostrando los errores el ultimo no muestra los errores.
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = RegisterUserCreateForm()
	return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

def editar_usuario(request, id_usuario):
	usuario = User.objects.get(pk = id_usuario)
	if request.method=='POST':
		formulario = EditarUserForm(request.POST, instance=usuario)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = EditarUserForm(instance = usuario)
	return render_to_response('editar-usuario.html', {'formulario':formulario, 'usuario':usuario}, context_instance=RequestContext(request))

def editar_perfil(request, id_perfil):
	perfil = PerfilUsuario.objects.get(id = id_perfil)
 	if request.method=='POST':
		formulario = EditarPerfilForm(request.POST, instance=perfil)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios/%s/perfiles' %perfil.usuario_id)
	else:
		formulario = EditarPerfilForm(instance = perfil)
	return render_to_response('editar_perfil.html', {'formulario':formulario, 'perfil':perfil}, context_instance=RequestContext(request))

def ver_usuario(request, id_usuario):	
	dato = User.objects.get(pk=id_usuario)
	return render_to_response('ver_usuario.html',{'usuario':dato},context_instance = RequestContext(request))

def ver_perfiles(request, id_usuario):	
	dato2 = PerfilUsuario.objects.filter(usuario=id_usuario)
	dato = User.objects.get(pk=id_usuario)
	return render_to_response('ver_perfiles.html',{'usuario':dato,'verPerfil':dato2},context_instance = RequestContext(request))

def nuevo_perfil(request, id_usuario):	
	dato = User.objects.get(pk=id_usuario)
	if request.method=='POST':
		formulario=PerfilForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios/%s/perfiles' %id_usuario)
	else: 
		formulario=PerfilForm()
	return render_to_response('nuevoperfil.html',{'formulario':formulario, 'dato':dato}, context_instance=RequestContext(request))

# login:
def ingresar(request):	
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
	usuario=request.user
	return render_to_response('privado.html',{'usuario':usuario},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/cerrar')

def ajax_username(request):
	ids = request.GET['clave']
	usuario = User.objects.get(username = ids)
	results = usuario.username
	data = json.dumps(results)
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)
#def ajax(request):
#	clave=request.GET["id_buscar"]
#	usuario=User.objects.get(pk=clave)
#	return HttpResponse(usuario.username)

def ajax(request):
	clave=request.GET["id_buscar"]
	usuario=User.objects.get(pk=clave)
	return HttpResponse(usuario.username)

def edit_estado(request):
	clave=request.POST["id_perfil_edit"]
	perfil = PerfilUsuario.objects.get(pk = clave)
	if request.method=='POST':
		formulario = EditarEstado(request.POST, instance=perfil)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios/%s/perfiles' %perfil.usuario_id)
	
def probandoajax(request):
	return render_to_response("probando_Ajax.html",context_instance=RequestContext(request))


