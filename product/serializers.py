from rest_framework import serializers
from .models import Category, Product, Review, Order, OrderItem
from rest_framework.exceptions import ValidationError

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    def validate_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError("Category does not exist!")
        return category_id
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    def validate_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist!")
        return product_id
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    def validate_id(self, review_id):
        try:
            Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise ValidationError("Review does not exist!")
        return review_id

    def validate_product(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist!")
        return product_id
    class Meta:

        model = Review
        fields = ['id', 'text', 'product']

class OrderItemListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    def validate_product(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist!")
        return product_id

    def validate_quantity(self, value):
        if value <= 0:
            raise ValidationError("Quantity must be greater than 0")
        return value
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    items =OrderItemListSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemDetailSerializer(many=True, read_only=True)
    def validate_customer_name(self, value):
        value = value.strip()
        if len(value) < 3:
            raise ValidationError("Customer name must be at least 3 characters")
        return value

    def validate_items(self, items):
        for item in items:
            try:
                Product.objects.get(id=item['product'].id)
            except Product.DoesNotExist:
                raise ValidationError(f"Product {item['product'].id} does not exist!")
            if item['quantity'] <= 0:
                raise ValidationError("Quantity must be greater than 0")
        return items
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'created_at', 'is_paid', 'items']
