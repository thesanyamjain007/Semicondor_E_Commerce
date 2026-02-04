from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from main.models import Product, Order

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')

def user_products(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def place_order(request, product_id):
    if not request.user.is_authenticated:
        return redirect('user_login')
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        Order.objects.create(user=request.user, product=product, quantity=quantity)
        messages.success(request, f"Order for {product.name} placed successfully!")
        return redirect('my_orders')
    return render(request, 'place_order.html', {'product': product})

def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    return render(request, 'my_orders.html', {'orders': orders})
