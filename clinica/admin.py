from django.contrib import admin
from .models import Especialidade, Medico, Cliente, Agenda, Consulta

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Cliente)
admin.site.register(Agenda)
admin.site.register(Consulta)