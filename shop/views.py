from django.shortcuts import render
from .models import Category, MenuItem


def home(request):
    categories = Category.objects.all()
    return render(request, "shop/home.html", {"categories": categories})


def hotmenu(request):
    items = MenuItem.objects.filter(category__name="Hot Drinks")
    return render(request, "shop/hot_drinks.html", {"items": items})


def coldmenu(request):
    items = MenuItem.objects.filter(category__name="Cold Drinks")
    return render(request, "shop/cold_drinks.html", {"items": items})


def foodmenu(request):
    items = MenuItem.objects.filter(category__name="Food")
    return render(request, "shop/food.html", {"items": items})


def about(request):
    return render(request, "shop/about.html")


def cart(request):
    return render(request, "shop/cart.html")
