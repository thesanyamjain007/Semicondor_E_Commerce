from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.view_users, name='admin_view_users'),
    path('add_product/', views.add_product, name='admin_add_product'),
    path('orders/', views.view_orders, name='admin_view_orders'),
    path('report/', views.sale_report, name='admin_sale_report'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
