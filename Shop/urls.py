from django.urls import path

from .views import (
     CategoryView, ProductView, ProductDetailsView,
     AddCategoryView, AddProductView, AddProductStockView,
)

app_name = 'shop'

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path('products/<int:cat_id>/', ProductView.as_view(), name='products'),
    path('product-details/<int:pro_id>/', ProductDetailsView.as_view(), name='product-details'),
    
    path('add-product/', AddProductView.as_view(), name='add-product'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('add-stock/<int:pro_id>/', AddProductStockView.as_view(), name='add-stock')
]