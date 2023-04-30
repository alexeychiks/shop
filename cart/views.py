from __future__ import annotations

from typing import TYPE_CHECKING

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from clothes import models

from .cart import Cart
from .forms import CartProductForm

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@require_POST
def cart_add(request: HttpRequest, product_id: int) -> HttpResponse:
    print(f'Adding product {product_id} to cart...')
    print(f'product_id is of type({type(product_id)})')

    print(f'Form data: {request.POST}')
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    form = CartProductForm(product.pk, data=request.POST)
    print('Validating form data...')
    if form.is_valid():
        cd = form.cleaned_data
        print(f'Form data is valid: {cd}')
        cart.add(product=product,
                 size=models.Size.objects.get(pk=cd['sizes']),
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect(reverse('cart:cart_detail'))
    print('Form data is invalid')


def cart_remove(request: HttpRequest, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    cart.remove(product)
    return redirect(reverse('cart:cart_detail'))


def cart_detail(request: HttpRequest):
    categories = models.Category.objects.all
    cart = Cart(request)
    # {'1': {'quantity': 1, 'price': '15000', 'size': 'XS'}}
    print(request.session['cart'])
    for item in cart:
        # {'quantity': 1, 'price': Decimal('15000'), 'size': 'XS',
        #  'product': <Product: Rockabilly Dress>, 'total_price': Decimal('15000')}
        print(item)
        item['update_quantity_form'] = CartProductForm(
            pk=item['product'].pk,
            initial={
                'size': item['size'],
                'quantity': item['quantity'],
                'update': True
            })
    return render(request, 'cart/detail.html', {
        'cart': cart,
        'categories': categories
    })
