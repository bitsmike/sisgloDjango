from django.contrib import admin
from .models import Distrito
from cenpobs.models import Cenpob

class CenpobInline(admin.StackedInline):
	model = Cenpob
	extra = 1


class DistritoAdmin(admin.ModelAdmin):
	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
	list_display = ('cod_distrito','name_distrito','prov',)
	list_filter = ('prov',)
	search_fields = ('cod_distrito', 'name_distrito', 'prov__name_provincia',)
	inlines = [CenpobInline, ]


# Register your models here.
admin.site.register(Distrito, DistritoAdmin)