from django.shortcuts import render,redirect
# from django.views.generic import ListView, DetailView
from .models import Cart

from addresses.forms import AddressForm
from accounts.forms import LoginForm,GuestForm
from accounts.models import GuestEmail
from billing.models import BillingProfile
from orders.models import Order
from products.models import Product

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart":cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            print("product is gone")
            redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None

    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_form = AddressForm()
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

# If there exists a billing_profile, we verify that the billing profile and cart we are using is the same as the session's billing profile and cart
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)


    context ={
    "object":order_obj,
    "billing_profile":billing_profile,
    "login_form":login_form,
    "guest_form":guest_form,
    "billing_address_form": billing_address_form,
    "address_form": address_form
    }

    return render(request, "carts/checkout.html", context)
