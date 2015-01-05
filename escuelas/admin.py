# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Escuela
from actions import export_as_excel

# Register your models here.
class EscuelaAdmin(admin.ModelAdmin):
	list_display = ('codmod','numero','nombre','nivel','director','celular','poblacion','distrito','escuela_ghp','provincia',)
	# list_editable = ('director','celular',)
	list_filter = ('escuela_ghp','nivel',)
	search_fields = ('codmod','numero','nombre','poblacion',)
	actions = (export_as_excel, )

admin.site.register(Escuela, EscuelaAdmin)