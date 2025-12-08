from Cart.models import CartModel

def cart_items(request):
    if request.user.is_authenticated:
        user_cart_items = request.user.carts.all()
        
        price = 0
        for items in user_cart_items:
            price += items.sub_total()
        
        print('total price', price)
        return {
            'user_cart_items': request.user.carts.all(),
            'total_price' : price
        }
    return {
        'user_cart_items': []
    }
