from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)
