from django.test import TestCase
from .models import Category, Order, OrderItem, Product, Festival 


class ProductsTest(TestCase):
	def test_product_list(self):
		r = self.client.get('/products/')
		self.assertEqual(r.status_code, 200)

	
	def test_order_list(self):
		festival = None
		r = self.client.get('/products/reports/orders/')
		self.assertEqual(r.status_code, 200)

	
	def test_order_list_with_festival(self):
		festival = 1
		r = self.client.get('/products/reports/orders/')
		self.assertEqual(r.status_code, 200)	


	def test_monthly_sales(self):
		r = self.client.get('/products/reports/monthly/')
		self.assertEqual(r.status_code, 200)


	def test_monthly_sales_previous(self):
		month = 'previous'
		r = self.client.get('/products/reports/monthly/')
		self.assertEqual(r.status_code, 200)


	def test_monthly_sales_last_three(self):
		month = 'three'
		r = self.client.get('/products/reports/monthly/')
		self.assertEqual(r.status_code, 200)


class ProductTestCase(TestCase):
	def setUp(self):
		Product.objects.create(
			product_name = 'Bastard Sword',
			product_size = 'S',
			product_quantity = 12,
			product_cost = 134.00,
			)


	def test_product_has_price(self):
		"""Products in the database have prices"""
		sword = Product.objects.get(product_name='Bastard Sword')
		self.assertEqual(sword.product_cost, 134.00)


	def test_product_has_size(self):
		"""Products in the database have sizes"""
		sword = Product.objects.get(product_name='Bastard Sword')
		self.assertEqual(sword.product_size, 'S')


	def test_product_has_quantity(self):
		"""Products in the database have quantities"""
		sword = Product.objects.get(product_name='Bastard Sword')
		self.assertEqual(sword.product_quantity, 12)	
