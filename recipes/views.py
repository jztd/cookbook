from django.shortcuts import render
from recipes.models import recipe, courses, ingredients, method
import recipes.views
# Create your views here.

def table_of_contents(request):
	# get all courses
	all_courses = courses.objects.all()
	# get all recipes
	recipe_list = recipe.objects.all()
	# save the view as a variable
	view = recipes.views.show_recipe
	
	return render(request, 'table_of_contents.html', {'courses' : all_courses , 'recipe' : recipe_list ,})


def show_recipe(request):
	# get the full path sent by the browser
	stuff = request.get_full_path()

	# split it again at the "=" in order to ge the recipe_name
	(var , recipe_name ) = stuff.split('show_recipe/')

	# replace the "%20" in the name with spaces so it matches the database
	recipe_name = recipe_name.replace('%20' , ' ' , 100)
	
	# find the recipe in the database by looking up the name
	recipe_name = recipe.objects.get(name__icontains = recipe_name)

	# now we get the ingredients related to the recipe by looking up the matching name
	ingredients_list = ingredients.objects.filter(related_recipe = recipe_name)

	# get the method from the database the same way
	method_list = method.objects.filter(related_recipe = recipe_name)
	image_list = recipe_name.image
	return render(request, 'hello.html', {'srecipe' : recipe_name , 'stuff' : stuff , 'course': recipe_name.course , 'ingredients' : ingredients_list , 'method' : method_list, 
		'image_list': image_list})

def new_recipe(request):
	host = request.META['REMOTE_ADDR']
	if 'term' in request.GET:
		term = request.GET['term']
		return render(request, 'new_recipe.html',{'host': host, 'term': term})
	else:
		return render(request, 'new_recipe.html', {'host': host ,})