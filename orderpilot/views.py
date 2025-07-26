from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser


# Create your views here.

def orders_view(request):
    if request.method == 'POST':
        orders_confirmed = Order.objects.filter(delivery_type="1")
        for order in orders_confirmed:
            order.confirmed = "1"
            order.save()
        return redirect('orders_view')
    return render(request,'orderpilot/ordersview.html')

def orders_list(request):
    if request.method == 'GET':
        orders = Order.objects.all().order_by('-id')
        serializer = OrderSerializer(orders,many=True)
        return JsonResponse(serializer.data,safe=False)
def order_detail(request,order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(order,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
