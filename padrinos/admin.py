# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Padrino

# Register your models here.
class PadrinoAdmin(admin.ModelAdmin):
	list_display = ('id','cod_padrino','nombres','apellidos','sede',)
	list_filter = ('apellidos','sede',)
	search_fields = ('cod_padrino','nombres','apellidos',)
	# action = (export_as_excel, )

admin.site.register(Padrino, PadrinoAdmin)