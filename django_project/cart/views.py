from django.shortcuts import render
from django.http import HttpResponseRedirect
from products.models import Product
from cart.models import Cart


# Create your views here.
def cart_index(request):
    try:
        carts = Cart.objects.filter(user=request.user)
    except TypeError:
        carts = None

    context = {
        'carts': carts,
    }
    return render(request, 'cart_index.html', context)


# Add one amount of product to cart.
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        # If there is no cart containing the product, create a new cart. Otherwise, increment the product_quantity and
        # re-calculate the total price.
        try:
            cart = Cart.objects.get(user=request.user, product=product)
            cart.product_qty += 1
            cart.total_price = cart.product_qty * product.price
            cart.save()
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user, product=product, product_qty=1, total_price=product.price)
            cart.save()
        except TypeError:
            cart = None

    return HttpResponseRedirect('/cart')


# Delete cart containing the product.
def delete_cart(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user, product=product)
        cart.delete()

    return HttpResponseRedirect('/cart')


# Delete one amount of product from the cart.
def delete_one_from_cart(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user, product=product)
        cart.product_qty -= 1
        cart.total_price = cart.product_qty * product.price
        cart.save()

    return HttpResponseRedirect('/cart')

