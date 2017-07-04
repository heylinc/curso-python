# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#Importar modelo
from documentos.models import Documento
#crear subclase de admin.ModelAdmin
class DocumentoAdmin(admin.ModelAdmin):
	model = Documento
#registrar modelAdmin para cada modelo
admin.site.register(Documento,DocumentoAdmin)