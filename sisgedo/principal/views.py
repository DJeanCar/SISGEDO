from principal.models import *
from principal.forms import RegisterUserCreateForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


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

def editar(request):
	variable='hj'
	if variable =='admin':
		return render_to_response('editar_adm.html', context_instance=RequestContext(request))
	return render_to_response('editar_user.html', context_instance=RequestContext(request))	
