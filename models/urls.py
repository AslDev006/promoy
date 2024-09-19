from django.urls import  path
from .views import home, form_page, about_us, products, contact_page, custom_404_view, success_page

handler404 = custom_404_view
urlpatterns = [
    path('', home, name="home_page"),
    path('about/', about_us, name="about_page"),
    path('form/', form_page, name="form_page"),
    path('success/', success_page, name="success_page"),
    path('products/', products, name="product_page"),
    path('contact/', contact_page, name="contact_page"),
]