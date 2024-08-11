from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.core.serializers import serialize

# Create your views here.

def home(request):
    q = Product.objects.all()
    data = serialize('json', q) 
    return HttpResponse(data, content_type="application/json")
    