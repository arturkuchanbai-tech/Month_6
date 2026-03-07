from django.contrib import admin
from .models import Category
from .models import Product
from .models import Review
from .models import Order
from .models import OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)