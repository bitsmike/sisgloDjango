# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Departamento, Provincia, Distrito, Centro_poblado

# Register your models here.
# @admin.register(Centro_poblado)

class Centro_pobladoAdmin(admin.ModelAdmin):
	list_display = ('codigo_cenpob','nombre_cenpob','CP_con_IE','nivel_ie','msnm','_Distrito','_Provincia','_Departamento',)
	#list_display_links = ('Distrito_Cenpob', )
	list_filter = ('departamento',)
	search_fields = ('nombre_cenpob','cp_dis_prov_dep','dep_prov_dis_cp',)
	# action = (export_as_excel, )
	raw_id_fields = ('distrito', 'provincia', 'departamento',)
	# inlines = [DistritoInline, ]

	def CP_con_IE(self, obj):
		return obj.con_ie == '1'
	CP_con_IE.boolean = True
	CP_con_IE.admin_order_field = 'con_ie'

class DistritoAdmin(admin.ModelAdmin):
	list_display = ('cod_distrito','name_distrito','provincia','departamento',)
	#list_display_links = ('Distrito_Cenpob', )
	list_filter = ('departamento',)
	search_fields = ('name_distrito',)
	# action = (export_as_excel, )
	raw_id_fields = ('provincia', 'departamento',)
	# inlines = [DistritoInline, ]

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('cod_provincia','name_provincia','departamento',)
	#list_display_links = ('Distrito_Cenpob', )
	list_filter = ('departamento',)
	search_fields = ('name_provincia',)
	# action = (export_as_excel, )
	raw_id_fields = ('departamento',)
	# inlines = [DistritoInline, ]

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('cod_departamento','name_departamento',)
	#list_display_links = ('Distrito_Cenpob', )
	search_fields = ('name_departamento',)
	# action = (export_as_excel, )
	# raw_id_fields = ('departamento',)
	# inlines = [DistritoInline, ]


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Centro_poblado, Centro_pobladoAdmin)