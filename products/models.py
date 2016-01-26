from django.db import models
from django.utils import timezone

class Product(models.Model):
	product_name = models.CharField(max_length=200)
	# these should be taken from the category table
	# in the database,but I'm sure how to do that just yet
	PRODUCT_CATEGORY_CHOICES = (
		("WEAPON", "Weapon"),
		("ARMOR", "Armor"),
		("ACCESORY", "Accesory")
	)
	product_category = models.CharField(max_length=30,
										choices=PRODUCT_CATEGORY_CHOICES)

	PRODUCT_SIZE_CHOICES = (
		("N", "None"),
		("S", "Small"),
		("M", "Medium"),
		("L", "Large")
	)
	product_size = models.CharField(max_length=1,
									choices=PRODUCT_SIZE_CHOICES,
									default = "N")
	product_quantity = models.IntegerField()
	product_cost = models.FloatField()


	def __str__(self):
		return self.product_name


class Category(models.Model):
	category_name = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = "Categories"


class Order(models.Model):
	order_date = models.DateField(auto_now_add=True)
	order_total = models.FloatField()


class OrderItem(models.Model):
	"""Represents and item that has been sold"""
	order_number = models.IntegerField()
	product_name = models.CharField(max_length=200)
	product_cost = models.FloatField()
	quantity_sold = models.IntegerField()


	class Meta:
		verbose_name_plural = "Order Items"



				
								