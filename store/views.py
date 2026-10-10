from rest_framework import status
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
def get_product(request, product_id):
    try:
        product = Product.objects.get(id = product_id)
        serializer = ProductSerializer(product, context = {'request': request})
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Product Not Found'}, status = status.HTTP_404_NOT_FOUND)


@api_view(['get'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)
    return Response(serializer.data)