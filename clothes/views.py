from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from cart.forms import CartProductForm
from clothes import models
from clothes.forms import LoginForm, Profile
from shop.settings import EMAIL_HOST_USER

from .forms import RegisterUserForm
from .token_generator import account_activation_token

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    products = models.Product.objects.all
    categories = models.Category.objects.all
    context = {'products': products,
               'categories': categories}
    return render(request, 'clothes/profile.html', context)


def index(request: HttpRequest) -> HttpResponse:
    pict = models.MainPictures.objects.all
    categories = models.Category.objects.all
    clothes = models.Product.objects.all
    products = models.Product.objects.all
    context = {
        'categories': categories,
        'clothes': clothes,
        'picture': pict,
        'products': products
    }
    return render(request, 'index.html', context)


def products(request: HttpRequest, slug: str) -> HttpResponse:
    categories = models.Category.objects.all
    category = models.Category.objects.get(url=slug)
    products = models.Product.objects.filter(category=category.id)
    context = {
        'products': products,
        'categories': categories,
        'category': category
    }

    return render(request, 'clothes/clothes.html', context)


def product(request: HttpRequest, product_url: str) -> HttpResponse:
    categories = models.Category.objects.all
    product = models.Product.objects.get(url=product_url)
    cart_form = CartProductForm(product.pk)
    context = {
        'product': product,
        'categories': categories,
        'cart_form': cart_form,
    }

    return render(request, 'clothes/info_clothes.html', context)


class BBLoginView(LoginView):
    form_class = LoginForm
    template_name = 'clothes/login.html'
    success_url = reverse_lazy('main')
    redirect_field_name = 'clothes/basic.html'
    products = models.Product.objects.all
    categories = models.Category.objects.all
    extra_context = {'products': products,
                     'categories': categories}


class BBLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'main'


def user_register(request: HttpRequest) -> HttpResponse:
    categories = models.Category.objects.all
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Активируйте свой аккаунт'
            message = render_to_string('clothes/register_done.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(email_subject, message, EMAIL_HOST_USER, [to_email])
            return render(request, 'clothes/send_confirm.html')
    else:
        form = RegisterUserForm()
    return render(request, 'clothes/register.html', {
        'form': form,
        'categories': categories
    })


def activate_account(request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
    categories = models.Category.objects.all
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = Profile.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Profile.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        template = 'clothes/activation_done.html'
    else:
        template = 'clothes/user_is_activated.html'
    return render(request, template, {'categories': categories})
