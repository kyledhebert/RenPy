from django.db import models
from django.utils import timezone

class Category(models.Model):
	"""Categories for product objects"""
	category_name = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category_name	

class Product(models.Model):
	product_name = models.CharField(max_length=200)
	product_category = models.ManyToManyField(Category)
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


class Festival(models.Model):
	"""Represents the different festivals the shop attends"""
	festival_name = models.CharField(max_length=250)
	festival_city = models.CharField(max_length=50)
	festival_state = models.CharField(max_length=2)

	def __str__(self):
		return self.festival_name



class Order(models.Model):
	"""Represents a completed order"""
	order_date = models.DateField(auto_now_add=True)
	order_total = models.FloatField()
	order_festival = models.ForeignKey(Festival, on_delete=models.CASCADE,)
	# the order_complete field will allow us to 
	# use an order object as both an order and cart
	order_complete = models.BooleanField()

	def __str__(self):
		return str(self.id)

	# will need a method for calculating order total
	def calculate_order_total():
		pass	


class OrderItem(models.Model):
	"""Represents and item that has been sold"""
	order_number = models.ForeignKey(Order, on_delete=models.CASCADE,)
	product_name = models.CharField(max_length=200)
	product_cost = models.FloatField()
	quantity_sold = models.IntegerField()


	class Meta:
		verbose_name_plural = "Order Items"

	def __str__(self):
		return self.product_name	
			