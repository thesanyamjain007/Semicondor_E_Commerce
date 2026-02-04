from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from main.models import Product, Order
from django.contrib import messages
from django.db.models import Sum

@staff_member_required
def view_users(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        
        Product.objects.create(
            name=name, description=description, price=price, 
            stock=stock, category=category, image=image
        )
        messages.success(request, f"Product {name} added successfully!")
        return redirect('collections')
    return render(request, 'add_product.html')

@staff_member_required
def view_orders(request):
    orders = Order.objects.all().order_by('-date_ordered')
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        status = request.POST.get('status')
        order = Order.objects.get(id=order_id)
        order.status = status
        order.save()
        messages.success(request, f"Order #{order_id} status updated to {status}.")
        return redirect('admin_view_orders')
    return render(request, 'orders_list.html', {'orders': orders})

@staff_member_required
def sale_report(request):
    delivered_orders = Order.objects.filter(status='Delivered')
    total_sales = delivered_orders.count()
    # Calculate revenue manually since price is on Product
    # A more robust way would be storing price at checkout in Order model
    total_revenue = 0
    for order in delivered_orders:
        total_revenue += order.product.price * order.quantity
        
    return render(request, 'report.html', {
        'total_sales': total_sales,
        'total_revenue': total_revenue,
        'orders': delivered_orders
    })

def admin_logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')
