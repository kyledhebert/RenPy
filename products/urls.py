from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
	# ex: /products/
	url(r'^$', views.index, name='index'),
	# ex: /products/2/
	url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name='detail'),
	url(r'^(?P<product_id>[0-9]+)/add_to_order/$',views.add_to_order,
			name='add_to_order')


	
]