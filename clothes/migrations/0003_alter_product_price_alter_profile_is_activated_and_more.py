# Generated by Django 4.1.1 on 2022-10-27 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_activated',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Проcто так'),
        ),
        migrations.CreateModel(
            name='ProductSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('off_price', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.product')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'размеры',
            },
        ),
    ]
