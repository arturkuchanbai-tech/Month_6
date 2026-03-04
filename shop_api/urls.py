"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import (
    category_list_view, category_detail_view,category_create_view,category_modify_view,
    product_list_view, product_detail_view,product_create_view,product_modify_view,
    review_list_view, review_detail_view,review_create_view,review_modify_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', category_list_view,name='category_list'),
    path('api/v1/categories/create/', category_create_view, name='category_create'),
    path('api/v1/categories/<int:id>/', category_detail_view, name='category_datail'),
    path('api/v1/categories/<int:id>/modify/', category_modify_view, name='category_modify'),
    path('api/v1/products/', product_list_view,name='product_list'),
    path('api/v1/products/create/', product_create_view, name='product_create'),
    path('api/v1/products/<int:id>/', product_detail_view, name='product_datail'),
    path('api/v1/products/<int:id>/modify/', product_modify_view, name='product_modify'),
    path('api/v1/reviews/', review_list_view,name='review_list'),
    path('api/v1/reviews/create/', review_create_view, name='review_create'),
    path('api/v1/reviews/<int:id>/', review_detail_view, name='review_datail'),
    path('api/v1/reviews/<int:id>/modify/', review_modify_view, name='review_modify'),


]

