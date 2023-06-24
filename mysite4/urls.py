
from django.contrib import admin
from django.urls import path
from order.views import order, order_search, order_list, update_order, meal_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path('order/', order, name='order'),
    path('order/search/', order_search, name='order_search'),
    path('orders/', order_list, name='order_list'),
    path('order/update/<int:order_id>/', update_order, name='update_order'),
    path('meal_create/', meal_create, name='meal_create'),
]
