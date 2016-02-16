from django.conf.urls import url


from . import views

app_name = 'products'
urlpatterns = [
    # ex: /products/
    url(r'^$', views.ProductListView.as_view(), name='product_list_view'),
    # ex: /products/2/
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(),
        name='product_detail_view'),
    url(r'^(?P<product_id>[0-9]+)/add_to_order/$',views.add_to_order,
        name='add_to_order'),
    # report urls
    url(r'^reports/orders/$', views.browse_orders, name='orders_list_view'),
    url(r'^reports/orders/(?P<festival>[0-9]+)/$', views.browse_orders, 
        name='orders_by_festival_list_view'),
    url(r'^reports/monthly/$', views.monthly_sales, name='monthly_sales'),
    url(r'^reports/monthly/(?P<month>[a-z]+)/$', views.monthly_sales,
        name='monthly_sales_by_month'),
    url(r'^reports/sales_over_time/$', views.sales_over_time, 
        name='sales_over_time'),


]