from django.contrib import admin
from .models import Ubigeocp

class UbigeocpAdmin(admin.ModelAdmin):
	#list_display = ('ubigeo','departamento','provincia','distrito','cenpob')
	fields = ('departamento','provincia','distrito','cenpob')
	#list_filter = ('departamento','provincia','distrito')



# Register your models here.
# admin.site.register(Ubigeocp, UbigeocpAdmin)