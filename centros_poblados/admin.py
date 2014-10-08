from django.contrib import admin
from .models import Departamento, Provincia, Distrito, Centro_poblado

# Register your models here.
class Centro_pobladoAdmin(admin.ModelAdmin):
	list_display = ('codigo_cenpob','nombre_cenpob','CP_con_IE','nivel_ie','msnm','_Distrito','_Provincia','_Departamento',)
	#list_display_links = ('Distrito_Cenpob', )
	#list_filter = ('distrito','provincia','departamento',)
	search_fields = ('nombre_cenpob','cp_dis_prov_dep','dep_prov_dis_cp',)
	# action = (export_as_excel, )
	# raw_id_fields = ('cod_dist', )
	# inlines = [DistritoInline, ]

	def CP_con_IE(self, obj):
		return obj.con_ie == '1'
	CP_con_IE.boolean = True
	CP_con_IE.admin_order_field = 'con_ie'

admin.site.register(Centro_poblado, Centro_pobladoAdmin)