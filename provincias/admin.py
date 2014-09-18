from django.contrib import admin
from .models import Provincia

class ProvinciaAdmin(admin.ModelAdmin):
	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
	list_display = ('cod_provincia','name_provincia','dep')
	#list_filter = ('departamento','provincia','distrito')


# Register your models here.
admin.site.register(Provincia, ProvinciaAdmin)