from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import *


class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historic'] = Historic.objects.all()
        context['carts'] = Cart.objects.all()
        return context
    
class RegisterProductView(CreateView):
    template_name = 'product/register_product.html'
    model = Product
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('product_detail', args=[self.object.pk])
    
    def form_valid(self, form):
        historic = Historic(activity=0, title='Inserção de Produto')
        historic.save()
        return super().form_valid(form)
    
class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    
class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    
class ProductUpdateView(UpdateView):
    template_name = 'product/product_update.html'
    model = Product
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('product_detail', args=[self.object.pk]) 
    
    def form_valid(self, form):
        historic = Historic(activity=1, title='Atualização de Produto')
        historic.save()
        return super().form_valid(form)
    
class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    
    def get_success_url(self):
        return reverse('product_list')
    
    def form_valid(self, form):
        historic = Historic(activity=2, title='Exclusão de Produto')
        historic.save()
        return super().form_valid(form)
    
    
class ClienteListView(ListView):
    template_name = 'client/client_list.html'
    model = Cliente
    
class RegisterClientView(CreateView):
    template_name = 'client/register_client.html'
    model = Cliente
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('client_detail', args=[self.object.pk])
    
    def form_valid(self, form):
        historic = Historic(activity=0, title='Inserção de Cliente')
        historic.save()
        return super().form_valid(form)
    
class ClienteDetailView(DetailView):
    template_name = 'client/client_detail.html'
    model = Cliente
    
class ClienteUpdateView(UpdateView):
    template_name = 'client/client_update.html'
    model = Cliente
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('client_detail', args=[self.object.pk])
    
    def form_valid(self, form):
        historic = Historic(activity=1, title='Atualização de Cliente')
        historic.save()
        return super().form_valid(form)
    
class ClienteDeleteView(DeleteView):
    template_name = 'client/client_delete.html'
    model = Cliente
    
    def get_success_url(self):
        return reverse('client_list')
    
    def form_valid(self, form):
        historic = Historic(activity=2, title='Exclusão de Cliente')
        historic.save()
        return super().form_valid(form)
    

class RegisterCartView(TemplateView):
    template_name = 'cart/register_cart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context
    
    def form_valid(self, form):
        historic = Historic(activity=0, title='Inserção de Carrinho')
        historic.save()
        return super().form_valid(form)
