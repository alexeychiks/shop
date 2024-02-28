from django import forms


class CartProductForm(forms.Form):
    class Meta:
        fields = ['quantity', 'size']
    def __init__(self, instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'] = forms.TypedChoiceField(choices=[(j.size, str(j.size)) for j in instance.size.all()],
                                                     label='размеры', coerce=int,
                                            )




