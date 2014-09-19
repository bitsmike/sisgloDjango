from django.contrib import admin
from .models import Ubigeocp

class UbigeocpAdmin(admin.ModelAdmin):
	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
	list_display = ('Codigo_Ubigeocp','Centro_poblado','distrito','provincia','municipio','departamento','pais',)
	#list_filter = ('departamento','provincia','distrito')
	list_filter = ('municipio', 'departamento', )
	search_fields = ('Centro_poblado__name_cenpob', )
	#action = (export_as_excel, )
	raw_id_fields = ('Centro_poblado','distrito','provincia','municipio','departamento',)

# Register your models here.
admin.site.register(Ubigeocp, UbigeocpAdmin)