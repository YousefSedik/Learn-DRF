from django.shortcuts import render
from rest_framework import generics
from products.product_serializer import ProductSerializers
from products.models import Product 
# Create your views here.

class ProductCreatAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
        
        return super(ProductCreatAPIView, self).perform_create(serializer)
    

class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    