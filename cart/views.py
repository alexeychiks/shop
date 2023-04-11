from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.urls import reverse

from .cart import Cart
from .forms import CartProductForm
from clothes import models

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    form = CartProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        cart.add(product=product, size=cd['size'], quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect(reverse('cart:cart_detail'))

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    cart.remove(product)
    return redirect(reverse('cart:cart_detail'))

def cart_detail(request):
    categories = models.Category.objects.all
    cart = Cart(request)
    print(request.session['cart'])
    for item in cart:
        print(item)
        item['update_quantity_form'] = CartProductForm(initial={'size':item['size'], 'quantity':item['quantity'], 'update':True})
    return render(request, 'cart/detail.html', {'cart':cart, 'categories': categories})