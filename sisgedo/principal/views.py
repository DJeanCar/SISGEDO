from principal.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import RegistrarUsuarioForm, PerfilForm, EditarUserFormAdm, EditarUserFormUser,EditarPerfilForm
from django.http import Http404
from django.utils import simplejson as json
from django.core import serializers 
from django import template


@login_required(login_url='/')
def usuarios(request):
	usuarios = User.objects.all()
	return render_to_response('usuarios.html', {'usuarios':usuarios}, context_instance=RequestContext(request))

@login_required(login_url='/')
def registrar_usuario(request):
	if request.method=='POST':
		formulario = RegistrarUsuarioForm(request.POST)
		#Hay diferencia entre is_valid() y is_valid, mientras que el primero valida mostrando los errores el ultimo no muestra los errores.
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios/')
	else:
		formulario = RegistrarUsuarioForm()
	return render_to_response('nuevo-usuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def editar_usuario(request, id_usuario):
	usuario = User.objects.get(pk = id_usuario)
	if request.method=='POST':
		formulario = EditarUserFormAdm(request.POST, instance=usuario)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = EditarUserFormAdm(instance = usuario)
	return render_to_response('editar-usuario.html', {'formulario':formulario, 'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/')
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

@login_required(login_url='/')
def ver_usuario(request):	
	clave=request.GET['id_usuario']
	usuario = User.objects.get(pk=clave) 
	data=json.dumps({'nombre':usuario.first_name,'apellido':usuario.last_name, 'email':usuario.email,'user':usuario.username,'direccion':usuario.direccion,'telefono':usuario.telefono})
	
	return HttpResponse(data, mimetype="application/json")

@login_required(login_url='/')
def ver_perfiles(request, id_usuario):	
	dato2 = PerfilUsuario.objects.filter(usuario=id_usuario)
	dato = User.objects.get(pk=id_usuario)
	return render_to_response('ver_perfiles.html',{'usuario':dato,'verPerfil':dato2},context_instance = RequestContext(request))

@login_required(login_url='/')
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

<<<<<<< HEAD

def home(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				user= User.objects.get(username=usuario)
				if acceso.is_active:
					if user.estado_login==True:
						return HttpResponseRedirect('/')
					else:
						login(request, acceso)
						user.estado_login=True
						user.save()
					return HttpResponseRedirect('/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('home.html',{'formulario':formulario}, context_instance=RequestContext(request))
					

=======
def home(request):
	if request.user.is_authenticated():
		usuario = request.user
		perfiles = PerfilUsuario.objects.filter(usuario = usuario)
		return render_to_response('home.html',{'perfiles':perfiles}, context_instance=RequestContext(request))
	else:
		if request.method == 'POST':
			formulario = AuthenticationForm(request.POST)
			if formulario.is_valid:
				usuario = request.POST['username']
				clave = request.POST['password']
				acceso = authenticate(username=usuario, password=clave)
				if acceso is not None:
					if acceso.is_active:
						login(request, acceso)
						return HttpResponseRedirect('/')
					else:
						return render_to_response('noactivo.html', context_instance=RequestContext(request))
				else:
					return render_to_response('nousuario.html', context_instance=RequestContext(request))
		else:
			formulario = AuthenticationForm()
		return render_to_response('home.html',{'formulario':formulario}, context_instance=RequestContext(request))
>>>>>>> 79cacd992b52a111ca081ef2122f5e91aa741ff2

@login_required(login_url='/')
def privado(request):
	usuario=request.user
	return render_to_response('privado.html',{'usuario':usuario},context_instance=RequestContext(request))

@login_required(login_url='/')
def cerrar(request):
<<<<<<< HEAD
	usuario=request.user
	usuario.estado_login=False
	usuario.save()
=======
	usuario = request.user
	try:
		perfiles = PerfilUsuario.objects.filter(usuario = usuario)
		if perfiles:
			for perfil in perfiles:
				perfil.online = False
				perfil.save()
		else:
			pass
	except:
		pass
>>>>>>> 79cacd992b52a111ca081ef2122f5e91aa741ff2
	logout(request)
	return HttpResponseRedirect('/')

def ajax_username(request):
	if request.is_ajax():
		username = request.GET['username']
		try:
			usuario = User.objects.get(username = username)
			data = usuario.username
		except:
			data = False
		return HttpResponse(data)
	else:
		raise Http404

def edit_estado(request):
	clave=request.POST["id_perfil_edit"]
	perfil = PerfilUsuario.objects.get(pk = clave)
	if perfil.estado == True:
		perfil.estado = False
	else:
		perfil.estado = True
	perfil.save()
	estado = perfil.estado
	return HttpResponse(estado)

def cambiar_online(request):
	if request.is_ajax():
		id_perfil = request.POST['id_perfil']
		try:
			perfil_elegido = PerfilUsuario.objects.get(pk = id_perfil)
			usuario = perfil_elegido.usuario
			perfiles = PerfilUsuario.objects.filter(usuario = usuario)
			for perfil in perfiles:
				if perfil.id == perfil_elegido.id:
					perfil.online = True
					perfil.save()
				else:
					perfil.online = False
					perfil.save()
			data = perfil_elegido.tipo
		except:
			data = False
		return HttpResponse(data)
	else:
		raise Http404

def resetear_clave(request):
	if request.is_ajax():
		id_usuario = request.POST["id"]
		try:
			usuario= User.objects.get(pk=id_usuario)
			usuario.set_password(usuario.username)
			usuario.save()
			dato=usuario.username
		except:
			dato=False
		return HttpResponse(dato)
	else:
		raise Http404



