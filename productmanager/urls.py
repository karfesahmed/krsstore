from django.urls import path
from . import views

urlpatterns = [
    path('super-krs-login',views.login_view,name="login"),
    path('addproduct',views.add_product,name="add_product"),
    path('super-krs-logout',views.logout_view,name="logout"),
    path('allproducts',views.all_products,name="all_products"),
    path('edit/<int:product_id>',views.edit_product,name="edit"),
    # API's
    path('wilayas',views.wilayas)
]