from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,HttpResponseForbidden
from .models import *
from .serializers import *
from costumerportal.models import *
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def login_view(request):
  message_error = None
  if request.user.is_authenticated  and request.user.is_superuser and request.user.is_staff:
    return HttpResponseRedirect(reverse('all_products'))
  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('all_products'))
    else:
      message_error = "Invalid Info !"
  return render(request,"productmanager/login.html",{
    "message":message_error
  })
def logout_view(request):
  logout(request)
  return redirect('login')

def add_product(request):
  if request.user.is_authenticated  and request.user.is_superuser and request.user.is_staff:
    categories = Category.objects.all()
    if request.method == 'POST':
      name = request.POST["name"]
      description = request.POST["description"]
      category = request.POST["category"]
      my_category = None
      if (category.strip() == "" and request.POST["new-category"].strip() != "")or(category.strip() != "" and request.POST["new-category"].strip() != "") :
        my_category = Category(name=request.POST["new-category"].strip())
        my_category.save()
      elif category.strip() != "" and request.POST["new-category"].strip() == "":
        my_category = Category.objects.get(name=category)
      else:
        my_category = None
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
  else:
    return HttpResponseForbidden("log in please")
def all_products(request):
  if request.user.is_authenticated  and request.user.is_superuser and request.user.is_staff:
    products = Product.objects.all().order_by('-id')
    return render(request,"productmanager/allproducts.html",{
      "products":products
    })
  else:
    return HttpResponseForbidden("log in please")

def edit_product(request,product_id):
  if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
    product = get_object_or_404(Product, pk=int(product_id))
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST["name"]
        description = request.POST["description"]
        category = request.POST["category"]
        new_category = request.POST["new-category"].strip()

        # التعامل مع الكاتيجوري
        if (category.strip() == "" and new_category != "") or (category.strip() != "" and new_category != ""):
            my_category = Category(name=new_category)
            my_category.save()
        elif category.strip() != "" and new_category == "":
            my_category = Category.objects.get(name=category)
        else:
            my_category = None

        price = float(request.POST["price"])
        images = request.FILES.getlist("images")
        colors = request.POST.getlist("color[]")
        color_images = request.FILES.getlist("color_image[]")
        exist_colors = request.POST.getlist("exist_color[]")
        sizes = request.POST.getlist("size[]")
        size_price = request.POST.getlist("size_price[]")
        sale_price = request.POST["sale_price"]
        is_active = request.POST.get("is_active") == "on"
        product.name = name
        product.description = description
        product.price = price
        product.category = my_category
        product.is_active = is_active
        if sale_price != "":
          product.sale_price = float(sale_price)
        else:
          product.sale_price = None
        product.save()

        
        if images:
          for img in product.images.all():
            if img.image:
              img.image.delete(save=False)  
            img.delete()
          for image in images:
            if image:
              img = Image(product=product, image=image)
              img.save()

        
        product.size.all().delete()
        for size, s_price in zip(sizes, size_price):
            if size.strip() != "":
                price_to_use = float(s_price) if s_price.strip() != "" else product.price
                s = Size(product=product, price=price_to_use, title=size)
                s.save()

        
        for color in product.colors.all():
          if color.title not in exist_colors:
            if color.image:
                color.image.delete(save=False)
            color.delete()
        
        counter = 0
        for color, exist_color in zip(colors, exist_colors):
            if exist_color == "not-exist":
              if color.strip() != "":
                c = Color(product=product, title=color, image=color_images[counter])
                c.save()
                counter += 1


        return redirect("all_products")

    return render(request, "productmanager/edit.html", {
        "product": product,
        "categories": categories
    })
  else:
    return HttpResponseForbidden("log in please")


def wilayas(request):
  if request.method == 'GET':
    wilayat = WilayaInfo.objects.all()
    serializer = WilayaInfoSerializer(wilayat,many=True)
    return JsonResponse(serializer.data,safe=False)
    


