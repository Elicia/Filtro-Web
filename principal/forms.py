#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from principal.models import PerfilUsuario

class RegistrarUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres')
    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser", "last_login", "groups", "user_permissions", "date_joined", 'password')

class EditarUserFormAdm(ModelForm):
    first_name = forms.CharField(label='Nombres')
    email= forms.EmailField(label="Email")
    is_active= forms.BooleanField(label="Usuario activo", required=False)
    username= forms.CharField(label="Nombre de usuario")
    class Meta:
        model = User
        exclude = ("is_staff","is_superuser","last_login", "groups", "user_permissions", "date_joined", 'password', 'password1', 'password2')

class EditarUserFormUser(ModelForm):
    first_name = forms.CharField(label='Nombres',widget = forms.TextInput(attrs={'readonly':'readonly'}))
    email= forms.EmailField(label="Email")
    username= forms.CharField(label="Nombre de usuario",widget = forms.TextInput(attrs={'readonly':'readonly'}))
    last_name=forms.CharField(label="Apellidos",widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        exclude = ("is_staff","is_active","is_superuser","last_login", "groups", "user_permissions", "date_joined", 'password', 'password1', 'password2')

class PerfilForm(ModelForm):
	class Meta:
		model=PerfilUsuario

class EditarPerfilForm(ModelForm):
    class Meta:
        model = PerfilUsuario