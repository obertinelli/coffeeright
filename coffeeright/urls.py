from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('coldmenu/', views.coldmenu, name="cold menu"),
    path('hotmenu/', views.hotmenu, name="hot menu"),
    path('foodmenu/', views.foodmenu, name="hot menu"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
]
