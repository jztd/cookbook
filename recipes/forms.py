from django import forms
from django.form import ModelForm
from django.db import models
from django.forms.models import modelformset_factory


class new_recipe_form(ModelForm):
	class Meta:
		model = recipe
		fields = ["name", "course"]

class recipe_method(ModelForm):
	class Meta:
		model = method
		fields = ["step"]

class recipe_ingredients(ModelForm):
	class Meta:
		model = ingredients
		fields = ["name"]

