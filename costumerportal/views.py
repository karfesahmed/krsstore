from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"costumerportal/home.html")

def products(request):
    return render(request,"costumerportal/products.html")
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