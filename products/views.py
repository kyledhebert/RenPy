from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Order, OrderItem, Product


def index(request):
	product_list = Product.objects.all()	
	context = {'product_list': product_list}
	return render(request, 'products/index.html', context)	

def product_detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)			
	return render(request, 'products/product_detail.html', {'product': product})


def add_to_order(request, product_id):
	"""Called when add to order is pressed on product detail page"""
	""" 
	TODO currently this create a new order every time,
	will need to implement session storage, and store the
	order number until an order is complete, and check
	for an existing order id before creating a new order

	"""
	# create a new order
	order = Order(order_total=0, order_complete=False)
	order.save()
	# get the product based on id
	product = Product.objects.get(pk=product_id)
	# create an order item using the new order number
	order_item = OrderItem(order_number=order.id,
							product_name=product.product_name,
							product_cost=product.product_cost,
							# TODO add this a value to POST
							# on product_detail page
							quantity_sold=1)
	order_item.save()
	# redirect to the order detail page
	return HttpResponseRedirect(reverse('products:index'))






