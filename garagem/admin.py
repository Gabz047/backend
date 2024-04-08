from django.contrib import admin
from .models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nacionalidade")
    search_fields = ("nome", "nacionalidade")
    list_filter = ("nome",)
    ordering = ("nome", "nacionalidade")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)


@admin.register(Acessorio)
class AcessorioAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ("nome", "marca" )
    search_fields = ("nome", "marca")
    list_filter = ("nome",)
    ordering = ("nome", "marca")


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("descricao", )
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)


