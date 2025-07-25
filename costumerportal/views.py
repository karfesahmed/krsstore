from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import *
from productmanager.models import WilayaInfo
from orderpilot.models import Order
# Create your views here.
def home(request):
    products = Product.objects.filter(is_active=True).order_by('-id')[:3]
    
    return render(request,"costumerportal/home.html",{
        "products":products
    })

def products(request):
    products = Product.objects.filter(is_active = True).order_by('-id')
    return render(request,"costumerportal/products.html",{
        "products":products
    })
def about_us(request):
    return render(request,"costumerportal/aboutus.html")
def contact_us(request):
    return render(request,"costumerportal/contactus.html")
def faqs(request):
    return render(request,"costumerportal/faqs.html")
def Privacy_Policy(request):
    return render(request,"costumerportal/privacy.html")

def thank_u_page(request):
    return render(request,"costumerportal/tup.html")

def product(request,product_id):
    try:
        product = Product.objects.get(pk=int(product_id))
    except Product.DoesNotExist:
        return HttpResponse("Product Does Not Exist")
    if request.method=='POST':
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        IDwilaya = request.POST.get("wilaya").split(",")[0]
        address = request.POST.get("address")
        quantity = int(request.POST.get("quantity"))
        color = request.POST.get("krs-option")
        size = None
        wilaya = WilayaInfo.objects.get(IDWilaya=IDwilaya)
        price = product.sale_price if product.is_on_sale() else product.price
        if  request.POST.get("size"):
            size = request.POST.get("size").split(",")[0]
            price = float(request.POST.get("size").split(",")[1])
        order = Order(
            product=product.name,
            wilaya = wilaya.name,
            IDwilaya = IDwilaya,
            Name = full_name,
            Phone = phone,
            Address = address,
            Size = size,
            Color = color,
            quantity = quantity,
            total = (price*quantity)+float(wilaya.delivery_home)
        )
        order.save()
        return redirect("tup")


    wilayas = WilayaInfo.objects.all()
    colors = Color.objects.filter(product = product)
    sizes = Size.objects.filter(product = product)
    return render(request,"costumerportal/product.html",{
        "product":product,
        "wilayas":wilayas,
        "colors":colors,
        "sizes" : sizes
    })

def category(request,category):
    category_selected = Category.objects.filter(name=category).first()
    products = category_selected.products.filter(is_active = True)
    return render(request,"costumerportal/category.html",{
        "products":products,
        "category":category
    })

# API's

def prod(request,product_id):
    if request.method == 'GET':
        product = Product.objects.get(pk=int(product_id))
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data,safe=False)
