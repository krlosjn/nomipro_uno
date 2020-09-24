from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
# Create your views here.

class RegistroEmpleado(CreateView):
  model=User
  template_name='usuario/registrar_form.html'
  form_class=RegistroForm
  success_url=reverse_lazy('inicio_listar')
  

