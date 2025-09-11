from django.shortcuts import render
from .models import Category, MenuItem


def home(request):
    categories = Category.objects.all()
    return render(request, "shop/home.html", {"categories": categories})


def hotmenu(request):
    items = MenuItem.objects.all()
    return render(request, "shop/hotmenu.html", {"items": items})


def coldmenu(request):
    items = MenuItem.objects.all()
    return render(request, "shop/coldmenu.html", {"items": items})


def foodmenu(request):
    items = MenuItem.objects.all()
    return render(request, "shop/foodmenu.html", {"items": items})


def about(request):
    return render(request, "shop/about.html")


def cart(request):
    return render(request, "shop/cart.html")
