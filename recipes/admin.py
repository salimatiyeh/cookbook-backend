from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cook_time', 'created_at')

admin.site.register(Recipe, RecipeAdmin)
