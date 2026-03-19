from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import (CategoryViewSet, ProductViewSet, ReviewViewSet, OrderViewSet, OrderItemViewSet)
router=DefaultRouter
router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)
router.register('orders', OrderViewSet)
router.register('orderitems', OrderItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
    path('users/', include('users.urls')),
]