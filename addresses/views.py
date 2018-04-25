from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from billing.models import BillingProfile
from .models import Address
from .forms import AddressForm

# Create your views here.
def checkout_address_create_view(request):
    address_form = AddressForm(request.POST or None)

    context = {
    "form": address_form
    }

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    print(address_form.is_valid())
    if address_form.is_valid():
        print(request.POST)
        instance = address_form.save(commit=False)
        billing_profile, created = BillingProfile.objects.new_or_get(request)

        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()

            request.session[address_type + "_address_id"] = instance.id
            print(address_type + "_address_id")

        else:
            print("Error: Billing profile was unable to be created")
            redirect("cart:checkout")

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
    return redirect("cart:checkout")

def checkout_address_reuse(request):
    if request.user.is_authenticated:
        context= {}
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        if request.method == "POST":
            address_type = request.POST.get('address_type', 'shipping')
            billing_profile, created = BillingProfile.objects.new_or_get(request)
            shipping_address = request.POST.get('shipping_address', None)
            if shipping_address is not None:
                qs = Address.objects.filter(billing_profile=billing_profile, id=shipping_address)
                if qs.exists():
                    request.session[address_type + "_address_id"] = shipping_address
                    print(redirect_path)
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
    return redirect("cart:checkout")
