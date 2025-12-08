from django.contrib import admin
from django.urls import path
from .views import AddToCart, CartView, RemoveCartItemView, DeleteCartItemView, CheckoutView, PaymentSuccessView, OrderDetailsView

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<int:pro_id>/', AddToCart.as_view(),name='add-to-cart'),
    path('cart-view/', CartView.as_view(), name='cart-view'),
    path('remove-cart/<int:cart_id>/', RemoveCartItemView.as_view(), name='remove-cart-item'),
    path('delete-cart/<int:cart_id>/', DeleteCartItemView.as_view(), name='delete-cart-item'),
    
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment-success/', PaymentSuccessView.as_view(), name='payment-success'),
    
    path('order/order-details', OrderDetailsView.as_view(), name='order-details'),
]

