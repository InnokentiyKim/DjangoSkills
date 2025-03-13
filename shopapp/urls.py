from django.urls import path
from .views import (GroupsListView, ShopIndexView, ProductDetailsView, ProductsListView, OrdersListView, create_product,
                    create_order, OrderDetailView, ProductCreateView, ProductUpdateView)

app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/create/', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_details'),
    path('orders/create/', create_order, name='orders_create'),
]