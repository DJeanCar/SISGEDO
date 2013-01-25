#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ("password", "is_staff", "is_superuser", "last_login", "groups", "user_permissions", "is_active", "date_joined")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user