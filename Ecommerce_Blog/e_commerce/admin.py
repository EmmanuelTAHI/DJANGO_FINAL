from django.contrib import admin
from .models import Categorie, Tag, Livre


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('nom',)
    list_filter = ('statut',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('nom',)
    list_filter = ('statut',)


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'isbn', 'langue', 'format', 'date_publication', 'categorie_ids')
    search_fields = ('titre', 'auteur', 'isbn')
    list_filter = ('langue', 'format', 'categorie_ids', 'tags_ids')
    autocomplete_fields = ['categorie_ids', 'tags_ids']
    date_hierarchy = 'date_publication'
