from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Festival

class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ('product_name',
					'product_size', 'product_quantity',
					'product_cost',)


class OrderAdmin(admin.ModelAdmin):
	model = Order
	list_display = ( Order,'order_date', 'order_festival', 'order_total',)


class OrderItemAdmin(admin.ModelAdmin):
	model = OrderItem
	list_display = ('order_number', 'product_name',
					'product_cost', 'quantity_sold',)	


class FestivalAdmin(admin.ModelAdmin):
	model = Festival
	list_display = ('festival_name', 'festival_city',
					'festival_state')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Festival, FestivalAdmin)