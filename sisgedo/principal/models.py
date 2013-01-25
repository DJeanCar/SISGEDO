from django.db import models
from django.contrib.auth.models import User

User.add_to_class('direccion', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('telefono', models.PositiveIntegerField(null=True,blank=True))


class PerfilUsuario(models.Model):
	TIPO=(
			('1','operario'),
			('2','supervisor'),
			('3','administrador'),
		)
	tipo = models.CharField(max_length=5,choices=TIPO)
	fecha_registro = models.DateField() 
	fecha_vigencia = models.DateField() 
	estado= models.BooleanField()
	usuario =models.ForeignKey(User)

	def __unicode__(self):
		return '%s y %s' %(self.usuario,self.tipo)