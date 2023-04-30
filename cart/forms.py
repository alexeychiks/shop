from django import forms
from django.forms import ModelForm

from clothes.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('sizes',)

    def __init__(self, pk: int, *args, **kwargs) -> None:
        super(CartProductForm, self).__init__(*args, **kwargs)
        print(f'kwargs: {kwargs}, pk: {pk}')
        sizes = Product.objects.get(pk=pk).sizes.all()
        sizes_list = [(size.id, size.size) for size in sizes]
        self.fields['sizes'] = forms.ChoiceField(choices=sizes_list)

        self.fields['quantity'] = forms.TypedChoiceField(
            choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='количество',
            initial=1, widget=forms.NumberInput(attrs={'min': '1', 'class': 'how_many'})
        )

        self.fields['update'] = forms.BooleanField(
            required=False, initial=False, widget=forms.HiddenInput)
