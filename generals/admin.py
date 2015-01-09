# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import General

# Register your models here.
class GeneralAdmin(admin.ModelAdmin):
	list_display = ('codigo_inicial',)
	#list_display_links = ('Distrito_Cenpob', )
	# list_filter = ('departamento',)
	# search_fields = ('nombre_cenpob','cp_dis_prov_dep','dep_prov_dis_cp',)
	# action = (export_as_excel, )
	raw_id_fields = ('escuela', 'poblacion', )
	# inlines = [DistritoInline, ]

admin.site.register(General, GeneralAdmin)