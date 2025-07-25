from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.http import JsonResponse
# Create your views here.

def orders_view(request):
    if request.method == 'POST':
        order_id = request.POST.get("order_id")
        order = Order.objects.get(pk=int(order_id))
        note = request.POST.get("note")
        type_delivery = request.POST.get("status")
        order_type = request.POST.get("shipping_to")
        new_quantity = request.POST.get("new_quantity")
        new_price = request.POST.get("new_price")
        order.note = note
        order.delivery_type = type_delivery
        order.order_type = order_type
        order.quantity = new_quantity
        order.total = new_price
        order.save()
        return redirect('orders_view')
    return render(request,'orderpilot/ordersview.html')

def orders_list(request):
    if request.method == 'GET':
        orders = Order.objects.all().order_by('-id')
        serializer = OrderSerializer(orders,many=True)
        return JsonResponse(serializer.data,safe=False)
