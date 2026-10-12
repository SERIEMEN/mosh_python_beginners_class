from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

#/products -> index
#uniform resource locator(address)

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products' : products})

# we are calling the render function with 3 arguments, the request object,
# the name of the template and a dictionary that the data is to be passed to in this template.

def new(request):
    return HttpResponse('New Products')


# Create your views here.
