from django.db import models

class Product(models.Model):
	product_name = models.CharField(max_length=200)
	PRODUCT_CATEGORY_CHOICES = (
		("WEAPON", "Weapon"),
		("ARMOR", "Armor"),
		("ACCESORY", "Accesory")
	)
	product_category = models.CharField(max_length=30,
										choices=PRODUCT_CATEGORY_CHOICES)

	PRODUCT_SIZE_CHOICES = (
		("S", "Small"),
		("M", "Medium"),
		("L", "Large")
	)
	product_size = models.CharField(max_length=1,
									choices=PRODUCT_SIZE_CHOICES)
	product_quantity = models.IntegerField()
	product_cost = models.FloatField()


	def __str__(self):
		return self.product_name
