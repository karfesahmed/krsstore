from django.urls import path
from . import views

urlpatterns = [
    path('zr-account',views.zr_account,name="zr_account")
]