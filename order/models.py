from django.db import models
from django.utils import timezone

class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    customer_phone = models.CharField(max_length=20)
    total_amount = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order} - {self.meal.name}'