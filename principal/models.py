from django.db import models

from django.contrib.auth.models import User

#Agregamos dos campos mas al modelo User que viene por defecto en Django.
User.add_to_class('pais', models.CharField(null=True,blank=True, max_length=500))


class PerfilUsuario(models.Model):

	nombre = models.CharField(max_length=20)
	fecha_registro = models.DateField(auto_now=True) 
	estado = models.BooleanField()
	online = models.BooleanField()

	usuario =models.ForeignKey(User)

	def __unicode__(self):
		return '%s y %s' %(self.usuario,self.nombre)

class Tag(models.Model):
	nombre = models.CharField(max_length=20)
	fecha_registro = models.DateField(auto_now=True) 
	perfil =models.ForeignKey(PerfilUsuario)

	def __unicode__(self):
		return '%s y %s' %(self.perfil,self.nombre)