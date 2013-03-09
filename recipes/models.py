from django.db import models



class courses(models.Model):
	name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ["name"]

class recipe(models.Model):
	course = models.ForeignKey(courses)
	name = models.CharField(max_length = 100)
	image = models.ImageField(upload_to ='images')

	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ["name"]

class ingredients(models.Model):
	name = models.CharField(max_length = 100)
	related_recipe = models.ForeignKey(recipe)

	def __unicode__(self):
		return self.name

class method(models.Model):
	step = models.CharField(max_length=500)
	related_recipe = models.ForeignKey(recipe)

	def __unicode__(self):
		return self.step



# Create your models here.
