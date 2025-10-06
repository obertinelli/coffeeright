from django.shortcuts import render
from .models import Category, MenuItem, Order


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
    try:
        order = Order.objects.latest('created_at')
        items = order.items.all()
        total = sum(item.price for item in items)
    except Order.DoesNotExist:
        items = []
        total = 0

    return render(request, "shop/cart.html", {"items": items, "total": total})