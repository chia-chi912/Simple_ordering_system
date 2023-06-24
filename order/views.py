from django.shortcuts import get_object_or_404, render, redirect
from .models import Meal, Order, OrderItem
import uuid

def generate_order_id():
    order_id = str(uuid.uuid4()).replace('-', '').upper()[:6]
    return order_id

def order(request):
    meals = Meal.objects.all()
    if request.method == 'POST':
        selected_meals = request.POST.getlist('meal')
        quantities = []
        for meal_id in selected_meals:
            quantity = request.POST.get('quantity{}'.format(meal_id))
            quantities.append(quantity)
        customer_phone = request.POST.get('customer_phone')
        notes = request.POST.get('note')
        
        # create
        order_id = generate_order_id()
        order = Order.objects.create(order_id=order_id, customer_phone=customer_phone, notes=notes)
        
        # save
        total_amount = 0
        for meal_id, quantity in zip(selected_meals, quantities):
            meal = Meal.objects.get(pk=meal_id)
            # 已勾選的餐點項目
            if quantity:
                OrderItem.objects.create(order=order, meal=meal, quantity=quantity)
                total_amount += meal.price * int(quantity)

        order.total_amount = total_amount if total_amount else 0.00
        order.save()
        
        return redirect('order_search')
    
    return render(request, 'order.html', {'meals': meals})

def order_search(request):
    if request.method == 'POST':
        customer_phone = request.POST.get('customer_phone')

        orders = Order.objects.filter(customer_phone=customer_phone).order_by('-created_at')

        return render(request, 'order_search.html', {'orders': orders})

    return render(request, 'order_search.html')

def order_list(request):
    orders = Order.objects.order_by('is_completed', 'created_at')
    return render(request, 'order_list.html', {'orders': orders})

def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # 切換訂單的完成狀態
    order.is_completed = not order.is_completed
    order.save()

    return redirect('order_list')

def meal_create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        
        # 創建訂單
        meal = Meal.objects.create(name=name, price=price)
        
        meal.save()
        
        return redirect('meal_create')
    
    return render(request, 'meal_create.html')