from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'home.html')

def collections(request):
    products = Product.objects.all()
    return render(request, 'collections.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
