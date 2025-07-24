from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from .serializers import *
from costumerportal.models import *
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def login_view(request):
  message_error = None
  if request.user.is_authenticated  and request.user.is_superuser and request.user.is_staff:
    return HttpResponseRedirect(reverse('add_product'))
  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('add_product'))
    else:
      message_error = "Invalid Info !"
  return render(request,"productmanager/login.html",{
    "message":message_error
  })
def logout_view(request):
  logout(request)
  return redirect('login')

def add_product(request):
  categories = Category.objects.all()
  if request.method == 'POST':
    name = request.POST["name"]
    description = request.POST["description"]
    category = request.POST["category"]
    my_category = None
    if category.strip() == "" and request.POST["new-category"].strip() != "":
      my_category, _ = Category.objects.get_or_create(name=request.POST["new-category"].strip())
    else:
      my_category = get_object_or_404(Category, name=category)
      my_category = Category.objects.get(name=category)
    price = float(request.POST["price"])
    images = request.FILES.getlist("images")
    colors = request.POST.getlist("color[]")
    color_images = request.FILES.getlist("color_image[]")
    sizes = request.POST.getlist("size[]")
    size_price = request.POST.getlist("size_price[]")
    product = Product(name=name,description=description,price=price,category=my_category)
    product.save()
    if images:
      for image in images:
        if image:
          img = Image(product=product, image=image)
          img.save()
    for size, s_price in zip(sizes, size_price):
      if size.strip() != "":
        price_to_use = float(s_price) if s_price.strip() != "" else product.price
        s = Size(product=product, price=price_to_use, title=size)
        s.save()
    for color, c_image in zip(colors, color_images):
      if color.strip() != "":
        c = Color(product=product, title=color, image=c_image)
        c.save()
    return redirect("all_products")  

  return render(request,"productmanager/addproduct.html",{
    "categories":categories
  })

def all_products(request):
  products = Product.objects.all()
  return render(request,"productmanager/allproducts.html",{
    "products":products
  })

def edit_product(request,product_id):
  try:
    product = Product.objects.get(pk=int(product_id))
  except Product.DoesNotExist:
    HttpResponse("product Does Not Exist")
  
  return render(request,"productmanager/edit.html",{
    "product":product
  })


def wilayas(request):
  if request.method == 'GET':
    wilayat = WilayaInfo.objects.all()
    serializer = WilayaInfoSerializer(wilayat,many=True)
    return JsonResponse(serializer.data,safe=False)
    


