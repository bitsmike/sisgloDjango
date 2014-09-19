from django.contrib import admin
from .models import Municipio

# Register your models here.
class MunicipioAdmin(admin.ModelAdmin):
	list_display = ('municipio_coordinacion', )
	search_fields = ('municipio_coordinacion', )

# Register your models here.
admin.site.register(Municipio, MunicipioAdmin)