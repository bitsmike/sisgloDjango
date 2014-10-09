from django.contrib import admin
from .models import Persona
from centros_poblados.models import Centro_poblado

class PersonaAdmin(admin.ModelAdmin):
	list_display=('dni','nombres','apellidos',)
	search_fields=('apellidos','nombres',)

# Register your models here.
admin.site.register(Persona,PersonaAdmin)