from django.contrib import admin
from .models import Category, OrderItem, Orders, Product, UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(UserProfile)