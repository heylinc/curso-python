# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.views.generic import View
from django.shortcuts import render

from documentos.models import Documento

class Documentos(View):
	def get(self, request, *args,**kwargs):

		docs = Documento.objects.all()

		context = {
		'docs': docs,
		'encabezado': 'Mis Documentos'

		}
		return render(request, 'documento.html', context)