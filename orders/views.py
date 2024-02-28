import hashlib

from cart.cart import Cart
from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem, Order
from django.core.mail import send_mail
from clothes.models import Category
from shop.settings import EMAIL_HOST_USER
# Create your views here.


def order_create(request):

    def calculate_signature(*args) -> str:
            return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()
    cart = Cart(request)
    print(cart.get_total_price())
    categories = Category.objects.all
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
    form = OrderCreateForm()
    signature = calculate_signature('danyabelolip', str(cart.get_total_price()), 0, '789456sugak')
    return render(request, 'orders/create_order.html',
                      {'cart': cart, 'form': form, 'categories': categories, 'signature': signature, })
            subject = 'Номер заказа: {}'.format(order.id)
            message = '{},\n\nВаш заказ был принят!\
                              ID вашего заказа: {}.'.format(order.first_name, order.id)
            send_mail(subject, message, EMAIL_HOST_USER, [order.email])
            price = cart.get_total_price()
            for item in cart:
                col = item['quantity']
                articul =item['product'].characteristic.articul
                size = item['size']



                mes = 'Заказ: {}\n почта клиента: {}\n{} X {} цена: {}р\nразмер: {}\nадресс доставки: {}'.format(order.id, order.email, col, articul, price,size, order.address )
                send_mail(subject, mes, EMAIL_HOST_USER, ['anyabelikaya@mail.ru'])
            cart.clear()


