from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, MenuItem


def home(request):  # makes homepage load
    categories = Category.objects.all()
    return render(request, "shop/home.html", {"categories": categories})


def hotmenu(request):  # makes hot drink menu page load
    items = MenuItem.objects.filter(category__name="Hot Drinks")
    return render(request, "shop/hot_drinks.html", {"items": items})


def coldmenu(request):  # makes cold drink menu page load
    items = MenuItem.objects.filter(category__name="Cold Drinks")
    return render(request, "shop/cold_drinks.html", {"items": items})


def foodmenu(request):  # makes food menu load
    items = MenuItem.objects.filter(category__name="Food")
    return render(request, "shop/food.html", {"items": items})


def about(request):  # makes about page load
    return render(request, "shop/about.html")


def add_to_cart(request, item_id):  # function for the cart
    item = get_object_or_404(MenuItem, id=item_id)
    order, created = Order.objects.get_or_create(is_complete=False)
    order.items.add(item)
    order.save()
    return redirect("cart")


def cart(request):
    cart = request.session.get("cart", {})
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    return render(request, "shop/cart.html", {"cart": cart, "total": total})


def remove_from_cart(request, item_id):
    cart = request.session.get("cart", {})
    if str(item_id) in cart:
        del cart[str(item_id)]
        request.session["cart"] = cart
    return redirect("cart")


def clear_cart(request):
    request.session["cart"] = {}
    return redirect("cart")
