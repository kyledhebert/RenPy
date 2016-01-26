from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
	# ex: /products/
	url(r'^$', views.index, name='index'),
	# ex: /products/2/
	url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name='detail')
	
]