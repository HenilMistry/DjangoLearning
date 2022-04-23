from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

# /Products page
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# /Products/new page
def new(request):
    return HttpResponse('This is new product page!')
