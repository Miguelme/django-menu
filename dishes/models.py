from django.db import models


class SpiceLevel(models.TextChoices):
	NONE = 'NONE', 'None'
	LOW = 'LOW', 'Low'
	MEDIUM = 'MED', 'Medium'
	HIGH = 'HIGH', 'High'


class Ingredient(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	category = models.CharField(max_length=64)
	imageUrl = models.URLField()

	def __str__(self):
		return self.name


class PriceableModel(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=512)
	category = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=16, decimal_places=2)
	imageUrl = models.URLField()
	notes = models.CharField(max_length=512, blank=True)
	isAvailable = models.BooleanField(default=True, verbose_name="Is Available?")
	ingredients = models.ManyToManyField(Ingredient, blank=True, related_name="%(class)singredients_ingredient")
	allergens = models.ManyToManyField(Ingredient, blank=True, related_name="%(class)sallergens_ingredients")
	spiceLevel = models.CharField(
		max_length=4,
		choices=SpiceLevel.choices,
		default=SpiceLevel.NONE
	)

	def __str__(self):
		return self.name

	class Meta:
		abstract = True


class Appetizer(PriceableModel):
	pass


class Dish(PriceableModel):
	pass


class Drink(PriceableModel):
	pass


class Desert(PriceableModel):
	pass
