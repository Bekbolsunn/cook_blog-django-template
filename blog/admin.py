from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at', 'id']
    inlines = [RecipeInline]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post', 'id']


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
