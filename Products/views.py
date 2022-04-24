from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.core.mail import send_mail

# Create your views here.

# /Products page
def index(request):
    # getting all products from database
    products = Product.objects.all()
    # passing the data in page and rendering on web-browser in reply
    return render(request, 'index.html', {'products': products})

# /Products/new page
def new(request):
    return HttpResponse('This is new product page!')

# /Products/send page
def send(request):
    send_mail('This is subject', 'This is body', '20ce054@charusat.edu.in', ['henilmistry74496@gmail.com'], fail_silently=True)
    return render(request, 'SendMail.html')
