from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db import transaction

from .utils import ViewSetCustom
from .serializers import *
from .models import *


class ProductViewSet(ViewSetCustom):
    
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        self.register_historic(
            title='Novo Produto Cadastrado',
            activity=0
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        self.register_historic(
            title='Produto Atualizado',
            activity=4
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        product.delete()
        
        self.register_historic(
            title='Produto Deletado',
            activity=8
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        self.register_historic(
            title='Produto Atualizado',
            activity=4
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return Product.objects.all()
    
    def get_serializer_class(self):
        return ProductSerializer

class ClienteViewSet(ViewSetCustom):
        
        def list(self, request):
            queryset = Cliente.objects.all()
            serializer = ClienteSerializer(queryset, many=True)
            return Response(serializer.data)
        
        def retrieve(self, request, pk=None):
            queryset = Cliente.objects.all()
            cliente = get_object_or_404(queryset, pk=pk)
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data)
        
        def create(self, request):
            serializer = ClienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            self.register_historic(
                title='Novo Cliente Cadastrado',
                activity=1
            )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def update(self, request, pk=None):
            queryset = Cliente.objects.all()
            cliente = get_object_or_404(queryset, pk=pk)
            serializer = ClienteSerializer(cliente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            self.register_historic(
                title='Cliente Atualizado',
                activity=5
            )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def destroy(self, request, pk=None):
            queryset = Cliente.objects.all()
            cliente = get_object_or_404(queryset, pk=pk)
            cliente.delete()
            
            self.register_historic(
                title='Cliente Deletado',
                activity=9
            )
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        def partial_update(self, request, pk=None):
            queryset = Cliente.objects.all()
            cliente = get_object_or_404(queryset, pk=pk)
            serializer = ClienteSerializer(cliente, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            self.register_historic(
                title='Cliente Atualizado',
                activity=5
            )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def get_queryset(self):
            return Cliente.objects.all()
        
        def get_serializer_class(self):
            return ClienteSerializer

class OrderViewSet(ViewSetCustom):
    
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return Order.objects.all()
    
    def get_serializer_class(self):
        return OrderSerializer
    
class PaymentMethodViewSet(ViewSetCustom):
    
    def list(self, request):
        queryset = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = PaymentMethod.objects.all()
        payment_method = get_object_or_404(queryset, pk=pk)
        serializer = PaymentMethodSerializer(payment_method)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = PaymentMethod.objects.all()
        payment_method = get_object_or_404(queryset, pk=pk)
        serializer = PaymentMethodSerializer(payment_method, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        queryset = PaymentMethod.objects.all()
        payment_method = get_object_or_404(queryset, pk=pk)
        payment_method.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, pk=None):
        queryset = PaymentMethod.objects.all()
        payment_method = get_object_or_404(queryset, pk=pk)
        serializer = PaymentMethodSerializer(payment_method, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return PaymentMethod.objects.all()
    
    def get_serializer_class(self):
        return PaymentMethodSerializer
    
class CartViewSet(ViewSetCustom):
        
    def list(self, request):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return Cart.objects.all()
    
    def get_serializer_class(self):
        return CartSerializer
    
    def create_order(self, items_dict, discount_rate):
        orders = []
        total_value = 0
        total_profit = 0
        discount_rate = float(discount_rate) / 100
        
        for item in items_dict:
            product = Product.objects.get(id=item['id'])
            subtotal = float(product.selling_price) * int(item['quantity'])
            discounted_total = subtotal - (subtotal * float(discount_rate))
            cost = float(product.buying_price) * int(item['quantity'])
            profit_after_discount = discounted_total - cost
            
            order = Order(
                product=product,
                quantity=item['quantity'],
                total=discounted_total,
                profit_total=profit_after_discount
            )
            
            total_value += discounted_total
            total_profit += profit_after_discount
            order.save()
            orders.append(order)
            
            # Atualiza o estoque
            product.stock -= int(item['quantity'])
            if product.stock < 0:
                return False, False, False
            product.save()
        
        return orders, total_value, total_profit
    
    def create_paymentMethod(self, payment_dict):
        payment = PaymentMethod(
            payment = payment_dict['method'],
            parcel = payment_dict['parcels'],
            discount = payment_dict['discount']
        )
        payment.save()
        return payment
    
    @action(methods=['post'], detail=False)
    def finish_cart(self, request):
        with transaction.atomic():
            payment_method = self.create_paymentMethod(request.data['payment'])
            orders, total_value, total_profit = self.create_order(request.data['items'], payment_method.discount)
            
            if not orders:
                return Response({'error': 'Estoque insuficiente'}, status=status.HTTP_400_BAD_REQUEST)
            
            
            cart = Cart(
                payment_method = payment_method,
                total = total_value,
                profit = total_profit,
                customer_name = request.data['customer_name'],
                customer_id = request.data['customer_id'],
                created_by_name = 'Admin'
            )

            cart.save()
            for order in orders:
                cart.orders.add(order)
            cart.save()
            
            serializer = CartSerializer(cart)
            
            self.register_historic(
                title='Compra finalizada',
                activity=3
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)