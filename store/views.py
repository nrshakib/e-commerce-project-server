from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer


@api_view(['get'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['get'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)
    return Response(serializer.data)