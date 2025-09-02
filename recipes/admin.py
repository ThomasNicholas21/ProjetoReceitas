from django.contrib import admin
from recipes.models import Recipe, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", f"{Recipe.__str__.__name__}", "title"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
