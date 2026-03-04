from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Category, Product, Review
from .serializers import (
    CategoryDetailSerializer, CategoryListSerializer,
    ProductDetailSerializer, ProductListSerializer,
    ReviewDetailSerializer, ReviewListSerializer
)

@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def category_detail_view(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)
@api_view(['POST'])
def category_create_view(request):
    serializer = CategoryDetailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['PUT', 'PATCH', 'DELETE'])
def category_modify_view(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = CategoryDetailSerializer(category, data=request.data, partial=(request.method=='PATCH'))
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def product_detail_view(request,id):
    product=get_object_or_404(Product,id=id)
    serializer=ProductDetailSerializer(product)
    return Response(serializer.data)
@api_view(['POST'])
def product_create_view(request):
    serializer = ProductDetailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['PUT','PATCH','DELETE'])
def product_modify_view(request,id):
    product = get_object_or_404(Product,id=id)

    if request.method =='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = ProductDetailSerializer(product,data =request.data, partial=(request.method=='PATCH'))
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def review_detail_view(request,id):
    review=get_object_or_404(Review,id=id)
    serializer=ReviewDetailSerializer(review)
    return Response(serializer.data)
@api_view(['POST'])
def review_create_view(request):
    serializer = ReviewDetailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['PUT','PATCH','DELETE'])
def review_modify_view(request,id):
    review = get_object_or_404(Review,id=id)

    if request.method =='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = ReviewDetailSerializer(review,data =request.data, partial=(request.method=='PATCH'))
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)