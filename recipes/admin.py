from django.contrib import admin
from recipes.models import recipe, courses, ingredients, method

class ingredientsInline(admin.StackedInline):
	model = ingredients
	extra = 3

class methodInline(admin.StackedInline):
	model = method
	extra = 1

class recipeAdmin(admin.ModelAdmin):
	list_display = ('name', 'course')
	search_fields = ('name', 'course')
	inlines = [ingredientsInline, methodInline, ]

admin.site.register(recipe, recipeAdmin)
admin.site.register(courses)