from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('products',views.products,name="products"),
    path('aboutus',views.about_us,name="aboutus"),
    path('contactus',views.contact_us,name="contactus"),
    path('faqs',views.faqs,name="faqs"),
    path('privacy',views.Privacy_Policy,name="privacy"),
    path('tup',views.thank_u_page,name="tup"),
    path('product/<int:product_id>',views.product,name="product"),

    # API's
    path('prod/<int:product_id>',views.prod)

]