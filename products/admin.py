from django.contrib import admin
from .models import Product, Category, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ('product_name',
					'product_size', 'product_quantity',
					'product_cost',)


class OrderAdmin(admin.ModelAdmin):
	model = Order
	list_display = ('order_date', 'order_total',)


class OrderItemAdmin(admin.ModelAdmin):
	model = OrderItem
	list_display = ('order_number', 'product_name',
					'product_cost', 'quantity_sold',)	

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)