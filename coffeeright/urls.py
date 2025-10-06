from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cold_drinks/', views.coldmenu, name="cold_drinks"),
    path('hot_drinks/', views.hotmenu, name="hot_drinks"),
    path('food/', views.foodmenu, name="food"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
]
