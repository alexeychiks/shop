from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField('Категория',max_length=150, null=True, blank=True)
    url = models.SlugField(max_length=160, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='Категория товара'
        verbose_name_plural = 'Категории товара'


class Characteristic(models.Model):
    articul = models.CharField(max_length=150, verbose_name='артикул', unique=True)
    image1 = models.ImageField('Изображение1', upload_to='static/clothes/images/', default='',blank=True)
    image2 = models.ImageField('Изображение2', upload_to='static/clothes/images/',default='',blank=True)
    image3 = models.ImageField('Изображение3', upload_to='static/clothes/images/',default='',blank=True)
    image4 = models.ImageField('Изображение4', upload_to='static/clothes/images/', default='', blank=True)
    image5 = models.ImageField('Изображение5', upload_to='static/clothes/images/', default='', blank=True)
    image6 = models.ImageField('Изображение6', upload_to='static/clothes/images/', default='', blank=True)
    sostav = models.TextField(verbose_name='Характеристика', null=True, blank=True)

    def __str__(self):
        return self.articul

    class Meta:
        verbose_name ='Характеристика'
        verbose_name_plural = 'Характеристики'

class Product(models.Model):
    name = models.CharField('Наименование', max_length=100)
    price = models.DecimalField('Цена',max_digits=10, decimal_places=0, default=0)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='static/clothes/images/')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    characteristic = models.ForeignKey('Characteristic', on_delete=models.SET_NULL, verbose_name='характеристика',
                                       null=True)
    available = models.BooleanField(default=False, verbose_name='наличие')
    size1 = models.BooleanField(default=False, verbose_name='42')
    size2 = models.BooleanField(default=False, verbose_name='44')
    size3 = models.BooleanField(default=False, verbose_name='46')
    size4 = models.BooleanField(default=False, verbose_name='48')
    url = models.SlugField(max_length=160, unique=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='Товар'
        verbose_name_plural = 'Товары'
class MainPictirues(models.Model):
    main_image1 = models.ImageField('Изображение1', upload_to='static/clothes/images/',default='')
    main_image2 = models.ImageField('Изображение2', upload_to='static/clothes/images/',default='')
    main_image3 = models.ImageField('Изображение3', upload_to='static/clothes/images/',default='')
    class Meta:
        verbose_name ='Картинка'
        verbose_name_plural = 'Картинки'

class Profile(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Проcто так')

    class Meta(AbstractUser.Meta):
        pass
