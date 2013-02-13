from django.db import models
from django.contrib.auth.models import User

#Agregamos dos campos mas al modelo User que viene por defecto en Django.
User.add_to_class('direccion', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('telefono', models.PositiveIntegerField(null=True,blank=True))
User.add_to_class('estado_login',models.BooleanField(default=False))


class PerfilUsuario(models.Model):
	TIPO=(
			('operario','operario'),
			('supervisor','supervisor'),
			('administrador','administrador'),
		)
	tipo = models.CharField(max_length=20,choices=TIPO)
	fecha_registro = models.DateField() 
	fecha_vigencia = models.DateField() 
	estado= models.BooleanField()
	usuario =models.ForeignKey(User)

	def __unicode__(self):
		return '%s y %s' %(self.usuario,self.tipo)
