from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cart, CartItem, Category, Product
from .serializer import CartSerializer, CategorySerializer, ProductSerializer


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

@api_view(['get'])
def get_cart(request):
    cart, created = Cart.objects.get_or_create(user = None)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['post'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    product = Product.objects.get(id = product_id)
    cart, created = Cart.objects.get_or_create(user = None)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()
    return Response({'message': 'Product added to cart', 'cart': CartSerializer(cart).data})

@api_view(['post'])
def remove_from_cart(request):
    item_id = request.data.get('item_id')
    CartItem.objects.filter(id = item_id).delete()
    return Response({'message':'Items removed from cart'})