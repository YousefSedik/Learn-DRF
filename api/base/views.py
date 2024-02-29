from django.shortcuts import render
from django.http import JsonResponse 
import json
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.product_serializer import ProductSerializers
# Create your views here.

@api_view(["POST"])
def api_home(request):
    """
     DRF API View. 
    """
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
    return Response(serializer.data)
