from django.urls import path
from . import views

urlpatterns=[
    path('orders',views.orders_view,name="orders_view"),
    path('tracking',views.tracking,name="tracking"),

    #API's
    path('orders-list',views.orders_list),
    path('order-detail/<int:order_id>',views.order_detail),
    path('zrorders',views.zrorders)
]