# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Documento(models.Model):
	#edad = models.IntegerField(null=True, blank=True)
	#fecha = models.DateTimeField(null= True, blank= True)
	nombre = models.CharField(max_length = 100, null = True, blank = True)
	fecha = models.DateTimeField(null = True, blank = True)


	def __unicode__(self):
		return 'Documento - {0}'.format(self.id)
