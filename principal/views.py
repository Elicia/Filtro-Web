from django.views.generic import TemplateView, DetailView, View
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from principal.forms import RegistrarUsuarioForm, EditarUserFormAdm, EditarUserFormUser,EditarPerfilForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from braces.views import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core import serializers

class RegistrarUsuario(FormView):
    template_name = 'principal/nuevo-usuario.html'
    form_class = RegistrarUsuarioForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegistrarUsuario, self).form_valid(form)


class MyLogin(View):

    def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/privado/")
			else:
				return render(request,'principal/noactivo.html')
		else:
			return render(request,'principal/nousuario.html')


class Cerrar(LoginRequiredMixin,View):
	login_url = '/'	

	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect('/')

class Privado(LoginRequiredMixin,TemplateView):
	login_url = '/'

	def get(self, request, *args, **kwargs):
		usuario=request.user
		return render(request,'principal/privado.html',{'usuario':usuario})



class UsuarioDetailView(LoginRequiredMixin,DetailView):
	model = User
	context_object_name = 'usuario'
	template_name = "principal/privado.html"
	login_url = '/'


class IndexAboutView(View):

    def get(self, request, *args, **kwargs):
		perfiles=PerfilUsuario.objects.filter(usuario=request.user.id)
		paginas =PaginaWeb.objects.all().order_by('orden_google')
		return render(request,'principal/index.html',{'perfiles':perfiles,'paginas':paginas})


class VerPerfiles(LoginRequiredMixin,TemplateView):
	login_url = '/'

	def get(self, request, *args, **kwargs):
		perfiles = PerfilUsuario.objects.filter(usuario=request.user.id)
		tags = Tag.objects.all()
		usuario=request.user.username
		return render(request,'principal/ver_perfiles.html',{'usuario':usuario,'perfiles':perfiles,'tags':tags})

class NuevoPerfil(TemplateView):

    def get(self, request, *args, **kwargs):
		return render(request,'principal/nuevoperfil.html')


def ajax_nuevo_perfil(request):
	print "buuuuuuuuuuuuuu"
	if request.is_ajax():
		print "es ajax"
		
		print "entro get"
		nom_perfil =request.POST['nom_perfil']
			# tags=request.POST['tags']
		print nom_perfil
			# print tags
			# dato = serializers.serialize('json', libros)
		data = True
		return HttpResponse(data)
	
	else:
		raise Http404
	

def ajax_busqueda(request):
	palabra_buscar = request.GET['palabra_buscar']

	try:
		pg = PalabraClave.objects.get(nombre=palabra_buscar)
		pg1 =pg.pwpclave_set.all().order_by('pagina_web__orden_google')
		ctx = {}	
		for a in pg1:
			print a.pagina_web.titulo
			ctx[a.pagina_web] = a.pagina_web.titulo	
		data = serializers.serialize('json', ctx,  fields=('titulo','contenido'))

	except :
		data = False
		print data
	return HttpResponse(data, mimetype="application/json")


class PaginaWebDetail(DetailView):
	model = PaginaWeb
	context_object_name = 'pw'
	template_name = "principal/detalle_pagina.html"

	def get(self, request, *args, **kwargs):
		get = super(PaginaWebDetail, self).get(request, *args,**kwargs)
		if request.user.is_authenticated():
			ver_si=UsuarioPagWeb.objects.filter(usuario=request.user.id,pagina_web=kwargs['pk']).count()
			if ver_si ==0:
				usu_pw=UsuarioPagWeb()
				usu_pw.usuario=request.user
				paginaweb=PaginaWeb.objects.get(id=kwargs['pk'])
				usu_pw.pagina_web=paginaweb
				usu_pw.save()
		return get

