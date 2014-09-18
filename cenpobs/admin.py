from django.contrib import admin
from cenpobs.models import Cenpob

class CenpobAdmin(admin.ModelAdmin):
	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
	list_display = ('cod_cenpob','name_cenpob',)
	#list_filter = ('departamento','provincia','distrito')
	search_fields = ('cod_cenpob', 'name_cenpob')

# Register your models here.
admin.site.register(Cenpob,CenpobAdmin)