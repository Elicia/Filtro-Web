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


class PaginaWeb(models.Model):
	tipo_pagina = models.CharField(max_length=20)
	orden_google = models.IntegerField()
	idioma= models.CharField(max_length=20)
	ubicacion= models.CharField(max_length=20)
	titulo = models.CharField(max_length=20)
	contenido = models.TextField()

	def __unicode__(self):
		return '%s y %s' %(self.titulo,self.orden_google)


class PalabraClave(models.Model):
	nombre = models.CharField(max_length=20)
	def __unicode__(self):
		return '%s' %(self.nombre)


class PwPclave(models.Model):
	pagina_web = models.ForeignKey(PaginaWeb)
	palabra_clave = models.ForeignKey(PalabraClave)

	def __unicode__(self):
		return '%s y %s' %(self.pagina_web,self.palabra_clave)


class UsuarioPagWeb(models.Model):
	usuario =models.ForeignKey(User)
	pagina_web = models.ForeignKey(PaginaWeb)

	def __unicode__(self):
		return '%s y %s' %(self.usuario,self.pagina_web)