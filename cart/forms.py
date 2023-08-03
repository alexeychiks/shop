from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
# GEEKS_CHOICES = [(j, str(j)) for j in range(42, 49, 2)]


class CartProductForm(forms.Form):
    class Meta:
        fields = ['quantity', 'size']
    def __init__(self, instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'] = forms.TypedChoiceField(choices=[(j.size, str(j.size)) for j in instance.size.all()], label='размеры', coerce=int)
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='количество',initial=1, widget=forms.NumberInput(attrs={'min': '1', 'class': 'how_many',})
    )

    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

