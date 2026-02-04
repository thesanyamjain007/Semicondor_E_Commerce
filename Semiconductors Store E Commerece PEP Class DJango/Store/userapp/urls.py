from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('products/', views.user_products, name='user_products'),
    path('place_order/<int:product_id>/', views.place_order, name='place_order'),
    path('my_orders/', views.my_orders, name='my_orders'),
]
