# Generated by Django 4.1.1 on 2023-08-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
