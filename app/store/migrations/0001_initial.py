# Generated by Django 5.1.3 on 2024-11-10 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField()),
                ('profit_total', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.IntegerField(choices=[(0, 'Cartão de Crédito'), (1, 'Cartão de Débito'), (2, 'Dinheiro'), (3, 'Pix')])),
                ('parcel', models.IntegerField(default=1)),
                ('discount', models.FloatField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do produto')),
                ('code', models.CharField(help_text='Código do produto', max_length=100, unique=True, verbose_name='Código do produto')),
                ('selling_price', models.FloatField(help_text='Preço que você deseja vender', verbose_name='Preço de venda')),
                ('buying_price', models.FloatField(help_text='Preço que o produto foi adiquirido para cálculo de lucro', verbose_name='Preço de compra')),
                ('stock', models.IntegerField(help_text='Quantidade total do produto em estoque', verbose_name='Estoque')),
                ('image', models.ImageField(blank=True, help_text='Imagem do produto', null=True, upload_to='products/', verbose_name='Imagem do produto')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('profit', models.FloatField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_id', models.IntegerField()),
                ('created_by_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('orders', models.ManyToManyField(to='store.order')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.paymentmethod')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
