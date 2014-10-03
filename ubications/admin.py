from django.contrib import admin
from .models import Ubication

class UbicationAdmin(admin.ModelAdmin):
	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
	list_display = ('Codigo_Ubication','Centro_poblado','distrito','provincia','departamento','pais',)
	#list_filter = ('departamento','provincia','distrito')
	list_filter = ('departamento', 'provincia', 'distrito', )
	search_fields = ('Centro_poblado__name_cenpob','cp_dis_prov_dep','dep_prov_dis_cp',)
	#action = (export_as_excel, )
	raw_id_fields = ('Centro_poblado','distrito','provincia','departamento',)

# Register your models here.
admin.site.register(Ubication, UbicationAdmin)