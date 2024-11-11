'''

Product
    - name
    - selling_price
    - buying_price

'''

from django.db import models


class Cliente(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do cliente')
    phone = models.CharField(max_length=100, verbose_name='Telefone do cliente', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='Endereço do cliente', null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email do cliente', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Data de modificação')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do produto')
    code = models.CharField(max_length=100, help_text='Código do produto', verbose_name='Código do produto', unique=True)
    selling_price = models.FloatField(help_text='Preço que você deseja vender', verbose_name='Preço de venda')
    buying_price = models.FloatField(help_text='Preço que o produto foi adiquirido para cálculo de lucro', verbose_name='Preço de compra')
    stock = models.IntegerField(help_text='Quantidade total do produto em estoque', verbose_name='Estoque')
    image = models.ImageField(upload_to='products/', null=True, blank=True, help_text='Imagem do produto', verbose_name='Imagem do produto')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField() # Valor total do pedido ( Com Desconto )
    profit_total = models.FloatField() # Lucro total do pedido
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
    

class PaymentMethod(models.Model):
    PAYMENT_METHODS = (
        (0, 'Cartão de Crédito'),
        (1, 'Cartão de Débito'),
        (2, 'Dinheiro'),
        (3, 'Pix'),
    )
    
    payment = models.IntegerField(choices=PAYMENT_METHODS)
    parcel = models.IntegerField(default=1)
    discount = models.FloatField(default=0)
    taxa = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.payment
    
    @property
    def payment_str(self):
        return self.get_payment_display()

class Cart(models.Model):
    orders = models.ManyToManyField(Order, related_name='orders', blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    total = models.FloatField() # Valor Pago
    profit = models.FloatField() # Lucro obtido
    customer_name = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    created_by_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
class Historic(models.Model):
    ACTIVITY_CHOICES = (
        (0, 'Inserir'),
        (1, 'Atualizar'),
        (2, 'Excluir'),
        (3, 'Venda'),
    )
    
    title = models.CharField(max_length=100)
    activity = models.IntegerField(choices=ACTIVITY_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def activity_str(self):
        return self.get_activity_display()