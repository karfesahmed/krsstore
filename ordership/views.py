from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseForbidden
# Create your views here.

def zr_account(request):
    if request.user.is_superuser:
        zraccount = Zr.objects.last()

        if request.method == 'POST':
            token = request.POST.get("token")
            key = request.POST.get("key")
            zr = Zr.objects.last()
            if zr:
                if zr.token == token and zr.key == key:
                    return redirect("zr_account")
            account = Zr(token=token,key=key)
            account.save()
        return render(request,"ordership/zraccount.html",{
            "zr_account":zraccount
        })
    else:
        return HttpResponseForbidden("log in please")

