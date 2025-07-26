from django.shortcuts import render,redirect
from .models import *
from ordership.models import Zr
from .serializers import *
from django.http import JsonResponse,HttpResponse,HttpResponseForbidden
from rest_framework.parsers import JSONParser
import requests
from django.contrib import messages
# Create your views here.

def orders_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            orders_confirmed = Order.objects.filter(delivery_type="1", confirmed="0")
            if not orders_confirmed.exists():
                return redirect('orders_view')
            zr = Zr.objects.last()
            if not zr:
                return redirect('zr_account')
            for order in orders_confirmed:
                order.confirmed = "1"
                order.save()

            orders = orders_confirmed
            Colis = []
            for order in orders:
                Colis.append({
                    "Tracking" : order.tracking_id(), 
                        "TypeLivraison" : order.order_type, # Domicile : 0 & Stopdesk : 1
                        "TypeColis" : "0",
                        "Confrimee" : "", # 1 pour les colis Confirmer directement en pret a expedier 
                        "Client" : order.Name,
                        "MobileA" : order.Phone,
                        "MobileB" : order.Phone,
                        "Adresse" : order.Address,
                        "IDWilaya" : order.IDwilaya,
                        "Commune" : "",
                        "Total" : order.total,
                        "Note" : order.note,
                        "TProduit" :  order.product,
                        "id_Externe" : order.id ,  # Votre ID ou Tracking 
                        "Source" : "" 
                })
            data = {
                    "Colis" : Colis
                }
            headers = {
                    "token": zr.token.strip(),  
                    "key": zr.key.strip(),  
                    "Content-Type": "application/json"
                }
            url = "https://procolis.com/api_v1/add_colis"
            response = requests.post(url,json=data,headers=headers)
            if response.status_code == 200:
                messages.success(request, "✅ The orders have been successfully sent to the shipping company!")
                for order in orders:
                    order.confirmed = "2"
                    order.save()
            else:
                messages.error(request, "❌ An error occurred while saving the orders. Please try again later.")
                for order in orders:
                    order.confirmed = "0"
                    order.save()
            return redirect('orders_view')
    
        return render(request,'orderpilot/ordersview.html')
    else:
        return HttpResponseForbidden("log in please")
def tracking(request):
    if request.user.is_superuser:
        return render(requests,"ordership/zrorders.html")
    else:
        return HttpResponseForbidden("log in please")

def orders_list(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            orders = Order.objects.all().order_by('-id')
            serializer = OrderSerializer(orders,many=True)
            return JsonResponse(serializer.data,safe=False)
    else:
        return HttpResponseForbidden("log in please")
def order_detail(request,order_id):
    if request.user.is_superuser:
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
    else:
        return HttpResponseForbidden("log in please")

def zrorders(request):
    if request.user.is_superuser:
        zr = Zr.objects.last()
        if not zr:
            return redirect('zr_account')
        
        trackings = Order.objects.filter(confirmed="2")
        trk = []
        for t in trackings:
            trk.append({"Tracking" : f"{t.tracking_id()}"})
        data = {
            "Colis" : trk
        }
        headers = {
            "token": zr.token.strip(),  
            "key": zr.key.strip(),  
            "Content-Type": "application/json"
        }
        url = "https://procolis.com/api_v1/lire"
        response = requests.post(url,json=data,headers=headers)
        
        return JsonResponse(response.json(),safe=False)
    else:
        return HttpResponseForbidden("log in please")