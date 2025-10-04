from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cold_drinks/', views.coldmenu, name="cold menu"),
    path('hot_drinks/', views.hotmenu, name="hot menu"),
    path('food/', views.foodmenu, name="food menu"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
]
