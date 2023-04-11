from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'pole'}))
    last_name = forms.CharField(label='Фамилия',widget=forms.TextInput(attrs={'class': 'pole'}))
    email = forms.EmailField(label='Почта',widget=forms.EmailInput(attrs={'class': 'pole'}))
    address = forms.CharField(label='Адресс',widget=forms.TextInput(attrs={'class': 'pole'}))
    postal_code = forms.CharField(label='индекс',widget=forms.TextInput(attrs={'class': 'pole'}))



    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code',
                  ]