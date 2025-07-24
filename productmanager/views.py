from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from .serializers import *
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
  return render(request,"productmanager/addproduct.html")


def wilayas(request):
  if request.method == 'GET':
    wilayat = WilayaInfo.objects.all()
    serializer = WilayaInfoSerializer(wilayat,many=True)
    return JsonResponse(serializer.data,safe=False)
    


