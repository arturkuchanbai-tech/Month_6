
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from django.shortcuts import get_object_or_404
from .models import Category, Product, Review,Order,OrderItem
from .serializers import (
    CategoryDetailSerializer, CategoryListSerializer,
    ProductDetailSerializer, ProductListSerializer,
    ReviewDetailSerializer, ReviewListSerializer,
    OrderItemDetailSerializer,OrderItemListSerializer,
    OrderDetailSerializer,OrderListSerializer
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        return CategoryDetailSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        return ReviewDetailSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return OrderDetailSerializer
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return OrderItemListSerializer
        return OrderItemDetailSerializer



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


@api_view(['GET'])
def order_list_view(request):
    orders = Order.objects.all()
    serializer = OrderListSerializer(orders, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def order_detail_view(request,id):
    order=get_object_or_404(Order,id=id)
    serializer=OrderDetailSerializer(Order)
    return Response(serializer.data)
@api_view(['POST'])
def order_create_view(request):
    serializer = OrderDetailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['PUT','PATCH','DELETE'])
def order_modify_view(request,id):
    order = get_object_or_404(Order,id=id)

    if request.method =='DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = OrderDetailSerializer(order,data =request.data, partial=(request.method=='PATCH'))
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)



@api_view(['GET'])
def orderitem_list_view(request):
    orderitems = OrderItem.objects.all()
    serializer = OrderItemListSerializer(orderitems, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def orderitem_detail_view(request,id):
    orderitem=get_object_or_404(OrderItem,id=id)
    serializer=OrderItemDetailSerializer(orderitem)
    return Response(serializer.data)
@api_view(['POST'])
def orderitem_create_view(request):
    serializer = OrderItemDetailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['PUT','PATCH','DELETE'])
def orderitem_modify_view(request,id):
    orderitem = get_object_or_404(OrderItem,id=id)

    if request.method =='DELETE':
        orderitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = OrderItemDetailSerializer(orderitem,data =request.data, partial=(request.method=='PATCH'))
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
