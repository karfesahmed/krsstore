from django.urls import path
from . import views

urlpatterns = [
    path('wilayas',views.wilayas)
]