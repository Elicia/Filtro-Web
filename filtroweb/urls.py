from django.conf.urls import patterns, include, url
from principal.views import IndexAboutView, MyLogin, Cerrar, Privado, UsuarioDetailView, RegistrarUsuario, VerPerfiles, NuevoPerfil
from django.contrib import admin
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexAboutView.as_view()),
    url(r'^login/$', MyLogin.as_view(), name='my_login'),
    url(r'^cerrar/$', Cerrar.as_view(),name='cerrar'),
    url(r'^privado/$',Privado.as_view(),name='privado'),
    url(r'^(?P<pk>\d+)/$', UsuarioDetailView.as_view(), name='detalle_usuario'),
    url(r'^nuevo/$', RegistrarUsuario.as_view(), name='nuevo'),
    url(r'^perfiles/$',VerPerfiles.as_view(), name='perfiles'),
	url(r'^perfiles/nuevo$',NuevoPerfil.as_view(), name='nuevo_perfil'),	
	url(r'^ajax_nuevo_perfil/$','principal.views.ajax_nuevo_perfil'),	
    url(r'^ajax_busqueda/$','principal.views.ajax_busqueda'),

	
)

