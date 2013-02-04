#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from principal.models import PerfilUsuario

class RegisterUserCreateForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres')
    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser", "last_login", "groups", "user_permissions", "date_joined", 'password')

class EditarUserForm(ModelForm):
    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser", "last_login", "groups", "user_permissions", "date_joined", 'password', 'password1', 'password2')

class PerfilForm(ModelForm):
	class Meta:
		model=PerfilUsuario

class EditarPerfilForm(ModelForm):
    class Meta:
        model = PerfilUsuario
        exclude=("usuario_id")

class EditarEstado(ModelForm):
    class Meta:
        model = PerfilUsuario
        exclude=("usuario_id","tipo","fecha_vigencia","fecha_registro")




        


