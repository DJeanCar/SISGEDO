#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from principal.models import PerfilUsuario

#RegisterUserCreateForm es un formulario que cambia el UserCreationForm
#para excluir algunos campos que no son necesarios para el sistema actual.
'''class RegisterUserCreateForm(UserCreationForm):
    first_name = forms.CharField(label = "Nombres", max_length=200)
    email = forms.EmailField(label = "Email")
    class Meta:
        model = User
        #Exclude nos ayuda a excluir algunos campos del modelo.
        exclude = ("is_staff", "is_superuser", "last_login", "groups", "user_permissions", "date_joined")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user'''

class RegisterUserCreateForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres')
    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser", "last_login", "groups", "user_permissions", "date_joined", 'password')

class PerfilForm(ModelForm):
	class Meta:
		model=PerfilUsuario

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario

        


