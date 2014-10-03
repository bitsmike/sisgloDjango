from django.contrib import admin
from .models import Departamento, Provincia, Distrito, Centro_poblado

# Register your models here.
# class Centro_pobladoAdmin(admin.ModelAdmin):
# 	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
# 	list_display = ('cod_cenpob','name_cenpob','CP_con_IE','nivel_ie','fuente_g','msnm','XGD','YGD','Distrito_Cenpob',)
# 	#list_display_links = ('Distrito_Cenpob', )
# 	list_filter = ('cod_dist','nivel_ie', )
# 	search_fields = ('cod_cenpob', 'name_cenpob', )
# 	action = (export_as_excel, )
# 	raw_id_fields = ('cod_dist', )
# 	# inlines = [DistritoInline, ]

# 	def CP_con_IE(self, obj):
# 		return obj.con_ie == '1'
# 	CP_con_IE.boolean = True
# 	CP_con_IE.admin_order_field = 'con_ie'

	# def get_ordering(self, request):
	# 	 if request.user.is_superuser:
 #            return ['name', 'rank']

# Register your models here.
admin.site.register(Departamento, Provincia, )