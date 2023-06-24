from django.contrib import admin
from .models import Meal, OrderItem, Order
# Register your models here.


admin.site.register(Meal)
admin.site.register(OrderItem)
admin.site.register(Order)

