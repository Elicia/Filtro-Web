from django.views.generic import TemplateView, DetailView, View
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from principal.forms import RegistrarUsuarioForm, PerfilForm, EditarUserFormAdm, EditarUserFormUser,EditarPerfilForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from braces.views import *

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


class IndexAboutView(TemplateView):
    template_name = "base.html"
