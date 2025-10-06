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
    path("add_to_cart/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("clear_cart/", views.clear_cart, name="clear_cart"),
]
