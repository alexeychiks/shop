from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from django.conf import settings

from clothes import models

if TYPE_CHECKING:
    from collections.abc import Generator

    from django.http import HttpRequest


class Cart(object):
    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self) -> Generator[dict]:
        product_ids = self.cart.keys()
        products = models.Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self) -> int:
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product: models.Product, size: models.Size,
            quantity: int = 1, update_quantity: bool = False) -> None:
        product_id = str(product.id)
        print(f'product_id: {product_id}')

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
                'size': str(size.size_code)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self) -> None:
        self.session.modified = True

    def remove(self, product: models.Product) -> None:
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self) -> Decimal:
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self) -> None:
        del self.session[settings.CART_SESSION_ID]
        self.save()
