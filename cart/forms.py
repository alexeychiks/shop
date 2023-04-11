from django import forms
from clothes.models import *

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

if Product.two:
    GEEKS_CHOICES = [(i, str(i)) for i in range(0,1)]


class CartProductForm(forms.Form):
    size = forms.TypedChoiceField(choices=GEEKS_CHOICES, label='размеры', coerce=int)
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='количество',initial=1, widget=forms.NumberInput(attrs={'min': '1', 'class': 'how_many',})
    )

    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

