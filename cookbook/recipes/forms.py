from django import forms
from django.forms import ModelForm
from recipes.models import recipe, method, ingredients
from django.forms.models import inlineformset_factory


class new_recipe_form(ModelForm):
	class Meta:
		model = recipe
		exclude = ('image')


#inline formsets

method_inline = inlineformset_factory(recipe, method, can_delete=False, extra=1)
ingredients_inline = inlineformset_factory(recipe, ingredients, can_delete=False, extra=1)