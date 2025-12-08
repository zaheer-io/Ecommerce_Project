from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View

from .models import CartModel, ProductModel, OrderModel, OrderItemsModel

from .forms import OrderForm

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import razorpay

import uuid

from django.http import HttpResponse




# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddToCart(View):
    def get(self,request, pro_id):
        cur_product = get_object_or_404(ProductModel, id=pro_id)
        cur_user = request.user
        
        try:
            cart = get_object_or_404(CartModel, user = cur_user, product = cur_product)
            cart.quantity += 1
            cart.save()
        except:
            CartModel.objects.create(user = cur_user, product = cur_product, quantity = 1)

        return redirect('cart:cart-view')

@method_decorator(login_required, name='dispatch')
class CartView(View):
    template_name = 'cart/cart.html'
    
    def get(self,request):
 
        cart_products = request.user.carts.all()
        
        total_price = 0
        for items in cart_products:
             total_price += items.sub_total() # items.product.product_price * items.quantity
        
        grand_total = total_price - 18
             
        return render(request, self.template_name, {'cart_products' : cart_products, 'total_price' : total_price})

@method_decorator(login_required, name='dispatch')
class RemoveCartItemView(View):
    def get(self, request, cart_id):
        current_item = get_object_or_404(CartModel, id=cart_id)

        current_item.quantity -= 1

        if current_item.quantity <= 0:
            current_item.delete()
        else:
            current_item.save()

        return redirect('cart:cart-view')

@method_decorator(login_required, name='dispatch')
class DeleteCartItemView(View):
    def get(self, request, cart_id):
        cart_item = get_object_or_404(CartModel, id=cart_id)
        cart_item.delete()
        return redirect('cart:cart-view')

@method_decorator(login_required, name='dispatch')
class CheckoutView(View):
    template_name = 'cart/checkout.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form' : OrderForm()})
    
    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user #user field
            
            cart_products = request.user.carts.all() 
            
            total_price = 0
            for items in cart_products:
                total_price += items.sub_total()
            
            order.amount = total_price # amount field
            
            order.save()
            
            if order.payment_method == 'Pay Online':
                client = razorpay.Client(auth = ('rzp_test_Rn84o8Z3bbux28', 'yVgDzj7J3Nn6xlPl3tzkNrRX')) 
                response_payment = client.order.create({'amount' : order.amount * 100, 'currency' : 'INR'})
                print(response_payment)
                
                order.order_id = response_payment['id']
                order.save()
                
                return render(request, 'cart/payment.html', {'payment' : response_payment})
            
            else:
                #updating order model
                
                cod_id = 'ORD_COD'+uuid.uuid4().hex[:14]
                order.order_id = cod_id
                order.is_ordered = True
                order.save()
                
                
                #Updating order items model
                cur_user_cart = request.user.carts.all()
                
                
                for item in cur_user_cart:
                    order_item = OrderItemsModel.objects.create(quantity = item.quantity, product = item.product, order = order)
                    order_item.save()
                    
                    order_item.product.stock -= item.quantity
                    order_item.product.save()
                
                cur_user_cart.delete()
                
                return render(request, 'cart/payment.html')
        
        return render(request, self.template_name, {'form' : form})

@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccessView(View):
    template_name = 'cart/payment-success.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print("Order Callback Received")
        
        print(request.user.username)
        print(request.POST)
        
        com_order = get_object_or_404(OrderModel, order_id = request.POST['razorpay_order_id'])
        com_order.is_ordered = True
        com_order.save()
        
        cur_user_cart = request.user.carts.all()
        
        for item in cur_user_cart:
            order_item = OrderItemsModel.objects.create(product = item.product, quantity = item.quantity, order = com_order)
            order_item.save()
            order_item.product.stock -= item.quantity
            order_item.product.save()
        
        cur_user_cart.delete()
        print('cart deleted')
        
        return render(request, self.template_name)

    
@method_decorator(login_required, name='dispatch')
class OrderDetailsView(View):
    template_name = 'cart/order/order-details.html'
    
    def get(self, request):
        order_details = request.user.orders.all()
        
        return render(request, self.template_name, {'order_details' : order_details})