from django.contrib import admin
from .models import Categoria

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nacionalidade")
    search_fields = ("nome", "nacionalidade")
    list_filter = ("nome",)
    ordering = ("nome", "nacionalidade")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao")
    search_fields = ("descricao")
    list_filter = ("descricao",)
    ordering = ("descricao")

