from django import forms
from django.forms import ModelForm
from recipes.models import recipe, method, ingredients
from django.forms.models import inlineformset_factory


class new_recipe(ModelForm):
	class Meta:
		model = recipe
		fields = ["course", "name"]


#inline formsets

method_inline = inlineformset_factory(recipe, method, can_delete=False, extra=20)
ingredients_inline = inlineformset_factory(recipe, ingredients, can_delete=False, extra=20)