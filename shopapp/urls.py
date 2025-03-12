from django.urls import path
from .views import GroupsListView, ShopIndexView, products_list, orders_list, create_product, create_order

app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/', products_list, name='products_list'),
    path('products/create/', create_product, name='products_create'),
    path('orders/', orders_list, name='orders_list'),
    path('orders/create/', create_order, name='orders_create'),
]