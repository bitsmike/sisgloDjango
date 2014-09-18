from django.contrib import admin
from .models import Departamento

class DepartamentoAdmin(admin.ModelAdmin):
	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
	list_display = ('cod_departamento','name_departamento')
	#list_filter = ('departamento','provincia','distrito')


# Register your models here.
admin.site.register(Departamento, DepartamentoAdmin)