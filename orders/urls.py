from django.urls import path
from orders.views import *


urlpatterns = [path('', order_create, name='order_create'),
               path('success', sucsess, name = 'success')
               ]