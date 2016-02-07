from datetime import datetime
from dateutil.relativedelta import *

from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic



from .models import Order, OrderItem, Product, Festival
from .forms import OrderDatesForm

def index(request):
	return render(request, 'products/index.html')


class ProductListView(generic.ListView):
	"""Generic ListView for displaying all products"""
	template_name = 'products/product_list.html'
	context_object_name = 'product_list'

	def get_queryset(self):
		"""Return the entire list of products."""
		return Product.objects.all()


class ProductDetailView(generic.DetailView):
	"""Generic DetailView for displaying indidual product detail page"""
	model = Product
	template_name = 'products/product_detail.html'


def browse_orders(request, festival=None):
	"""A list of all orders, or orders from a specific festival"""

	# get the festivals from the database, to display browse options
	festival_list = Festival.objects.all()

	if festival:
		orders_list = Order.objects.filter(order_festival=festival)
	else:
		orders_list = Order.objects.all()

	return render(request, 'products/orders.html', {
		'festival_list': festival_list,
		'orders_list': orders_list,
		'festival': festival,
		})


def monthly_sales(request, month=None):
	"""A report of sales totals a single month"""

	def get_total_sales(orders_list):
		return orders_list.aggregate(Sum('order_total'))

	# first determine today, all dates below based on today
	today = datetime.now()

	# then filter Order objects based on parameter

	if month == 'previous':
		# use relativedelta to get last month
		last_month = today + relativedelta(months=-1)
		orders_list = Order.objects.filter(order_date__year=today.year,
			order_date__month=last_month.month)
		total_sales = get_total_sales(orders_list)
	
	elif month == 'three':
		start_date = today + relativedelta(months=-3)
		orders_list = Order.objects.filter(order_date__range=(start_date, today))
		total_sales = get_total_sales(orders_list)	
	else:
		orders_list = Order.objects.filter(order_date__year=today.year,
			order_date__month=today.month)
		total_sales = get_total_sales(orders_list)

	return render(request, 'products/monthly_sales.html', {
		'orders_list': orders_list,
		'total_sales': total_sales,
		})


def sales_over_time(request):
	"""Generates a report of sales over a specified period"""

	def get_total_sales(orders_list):
		return orders_list.aggregate(Sum('order_total'))


	# if this is a POST request, process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = OrderDatesForm(request.POST)
		#check whether the form is valid 
		if form.is_valid():
			# use the data in form.cleaned_data to make the query set
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']
			orders_list = Order.objects.filter(order_date__range=(start_date,end_date))
			total_sales = get_total_sales(orders_list)
	# if this is a GET create a blank form
	else:
		form = OrderDatesForm()
		# default report will be for last 30 days
		end_date = datetime.now()
		start_date = end_date + relativedelta(months=-1)
		orders_list = Order.objects.filter(order_date__range=(start_date,end_date))
		total_sales = get_total_sales(orders_list)	
		
	return render(request, 'products/sales_over_time.html', {
		'form': form,
		'orders_list': orders_list,
		'total_sales': total_sales
		})	


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
	return HttpResponseRedirect(reverse('products:product_list_view'))






