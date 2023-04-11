from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import Profile
from django.forms import ModelForm
from .models import Product


class LoginForm(AuthenticationForm):
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'pole'}))
        email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'pole'}))
        password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'pole'}))
        class Meta:
            model = Profile
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if email and Profile.objects.filter(email=email).exists():
                #raise forms.ValidationError(u'Email addresses must be unique.')
               return email
            else:
                raise forms.ValidationError('Неправильная почта')
        def clean_username(self):
            username = self.cleaned_data.get('username')
            if username and Profile.objects.filter(username=username).exists():
                #raise forms.ValidationError(u'Email addresses must be unique.')
               return username
            else:
                raise forms.ValidationError('Неправильный логин')




class RegisterUserForm(forms.ModelForm):
     username = forms.CharField(required=True,
                             label='Логин', widget=forms.TextInput(attrs={'class': 'pole'}))
     email = forms.EmailField(required=True,
     label='Почта', widget=forms.EmailInput(attrs={'class': 'pole'}))
     password1 = forms.CharField(label='Пароль',
     widget=forms.PasswordInput(attrs={'class': 'pole'}))
     password2 = forms.CharField(label='Пароль (повторно)',
     widget=forms.PasswordInput(attrs={'class': 'pole'}))

     def clean(self):
          super().clean()
          password1 = self.cleaned_data['password1']
          password2 = self.cleaned_data['password2']
          if password1 and password2 and password1 != password2:
              errors = {'password2': ValidationError(
              'Введенные пароли не совпадают', code='password_mismatch')}
              raise ValidationError(errors)

     def clean_email(self):
         email = self.cleaned_data.get('email')
         if email and Profile.objects.filter(email=email).exists():
                raise forms.ValidationError('Пользователь с такой почтой существует')
         return email

     def clean_username(self):
         username = self.cleaned_data.get('username')
         if username and Profile.objects.filter(username=username).exists():
             # raise forms.ValidationError(u'Email addresses must be unique.')
             raise forms.ValidationError('Неправильный логин')
         else:
             return username
     class Meta:
       model = Profile
       fields = ('username','email','password1', 'password2',
       )
