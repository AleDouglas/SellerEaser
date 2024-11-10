from django.urls import path
from rest_framework import routers
from .views import *
from .api import *

router = routers.DefaultRouter()
router.register(r'v1/product', ProductViewSet, basename='product')
router.register(r'v1/client', ClienteViewSet, basename='client')
router.register(r'v1/order', OrderViewSet, basename='order')
router.register(r'v1/payment', PaymentMethodViewSet, basename='payment')
router.register(r'v1/cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/register/', RegisterProductView.as_view(), name='register_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    
    path('client/', ClienteListView.as_view(), name='client_list'),
    path('client/register/', RegisterClientView.as_view(), name='register_client'),
    path('client/<int:pk>/', ClienteDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/update/', ClienteUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClienteDeleteView.as_view(), name='client_delete'),
    
    
    path('cart/register/', RegisterCartView.as_view(), name='register_cart'),
]

urlpatterns += router.urls
