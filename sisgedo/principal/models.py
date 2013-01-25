from django.db import models
from django.contrib.auth.models import User

#Agregamos dos campos mas al modelo User que viene por defecto en Django.
User.add_to_class('direccion', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('telefono', models.PositiveIntegerField(null=True,blank=True))