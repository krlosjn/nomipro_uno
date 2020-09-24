from django.conf.urls import url
from apps.usuario.views import RegistroEmpleado

#Create your url 

urlpatterns = [
    url(r'^nuevo$', RegistroEmpleado.as_view(), name="registrar"),
]
