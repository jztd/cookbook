from django.shortcuts import render, redirect
from recipes.models import recipe, courses, ingredients, method
from recipes.forms import new_recipe_form, method_inline, ingredients_inline

def table_of_contents(request):
	# get all courses
	all_courses = courses.objects.all()
	# get all recipes
	recipe_list = recipe.objects.all()

	return render(request, 'table_of_contents.html', {'courses' : all_courses , 'recipe' : recipe_list})


def show_recipe(request):
	# get the full path sent by the browser
	stuff = request.get_full_path()

	# split it again at the "=" in order to ge the recipe_name
	(var , recipe_name ) = stuff.split('show_recipe/')

	# replace the "%20" in the name with spaces so it matches the database
	recipe_name = recipe_name.replace('%20' , ' ' , 100)
	
	# find the recipe in the database by looking up the name
	recipe_name = recipe.objects.get(name = recipe_name)

	# now we get the ingredients related to the recipe by looking up the matching name
	ingredients_list = ingredients.objects.get(related_recipe = recipe_name)

	# get the method from the database the same way
	method_list = method.objects.get(related_recipe = recipe_name)
	image_list = recipe_name.image
	return render(request, 'hello.html', {'srecipe' : recipe_name , 'stuff' : stuff , 'course': recipe_name.course , 'ingredients' : ingredients_list , 'method' : method_list, 
		'image_list': image_list})

def new_recipe(request):
	if request.method == 'POST':
		form = new_recipe(request.POST)
		if form.is_valid():
			Recipe = form.save(commit=False)
			ingredients_form = ingredients_inline(request.POST, instance=Recipe)
			method_form = method_inline(request.POST, instance=Recipe)
			if ingredients_form.is_valid() and method_form.is_valid():
				recipe.save()
				ingredients_form.save()
				method_form.save()
				return render(request, 'table_of_contents.html',{})
	else:
		form = new_recipe_form()
		method_form = method_inline(instance=recipe())
		ingredients_form = ingredients_inline(instance=recipe())
	return render(request, 'new_recipe.html', {'new_recipe_form': new_recipe_form, 'method_form': method_form, 'ingredients_form': ingredients_form } )

