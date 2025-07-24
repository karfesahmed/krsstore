from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import *
from productmanager.models import WilayaInfo
# Create your views here.
def home(request):
    products = Product.objects.all()[:3]
    
    return render(request,"costumerportal/home.html",{
        "products":products
    })

def products(request):
    products = Product.objects.all()
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
    products = category_selected.products.all()
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
