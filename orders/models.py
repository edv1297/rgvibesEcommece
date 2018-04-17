from django.db import models
from carts.models import Cart
from django.db.models.signals import pre_save, post_save
from rshop.utils import unique_order_id_generator
from billing.models import BillingProfile
from addresses.models import Address

ORDER_STATUS_CHOICES = (
    ('created', 'Order has been created'),
    ('processing', 'Payment is processing'),
    ('paid', 'Payment is verified'),
    ('packaged', 'We are getting your package together'),
    ('delivered', 'Your package is out for delivery'),
    ('received', 'Your package has made it to its end location, enjoy!'),
    ('refunded_processing', 'We are processing your order for a refund'),
    ('cancelled', 'Your order has been successfully cancelled'),
)

class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        qs = self.get_queryset().filter(
                        billing_profile=billing_profile,
                        cart = cart_obj,
                        active = True,
                        status = 'created')
        created = False
        if qs.count()==1:
            obj = qs.first()
        # no billing profile exists, make a new order or update the old one to have the billing profile of the session
        else:
            obj = self.model.objects.create(billing_profile = billing_profile, cart = cart_obj, active= True)
            created= True
        return obj, created

class Order(models.Model):
    order_id            = models.CharField(max_length= 120, blank = True)
    shipping_address    = models.ForeignKey(Address, related_name = 'shipping_address', null = True, blank = True)
    billing_address     = models.ForeignKey(Address, related_name = 'billing_address', null = True, blank = True)
    cart                = models.ForeignKey(Cart)
    status              = models.CharField(max_length = 120, default = 'created', choices = ORDER_STATUS_CHOICES)
    total               = models.DecimalField(default = 0.00, max_digits = 8, decimal_places = 2)
    shipping_total      = models.DecimalField(default = 5.99, max_digits = 8, decimal_places = 2)
    billing_profile     = models.ForeignKey(BillingProfile, null = True, blank = True)
    active              = models.BooleanField(default = True)

    def __str__(self):
        return self.order_id

    objects = OrderManager()

    def update_total(self):
        cart_total= self.cart.total
        shipping_total = self.shipping_total
        new_total = float(cart_total) + float(shipping_total)
        self.total = new_total
        self.save()
        return  new_total

    def check_done(self):
        billing_profile     = self.billing_profile
        shipping_address    = self.shipping_address
        billing_address     = self.billing_address
        total               = self.total

        if billing_profile and shipping_address and billing_address and total > 0:
            return True
        return False

    def mark_paid(self):
        if self.check_done():
            self.status = 'paid'
            self.save()
            return self.status
        else:
            self.status = 'processing' 
            self.save()
            return self.status

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance) # generate the order id
    # deactivate a cart if we find a cart with the same billing profile
    qs = Order.objects.filter(cart = instance.cart).exclude(billing_profile = instance.billing_profile)
    if qs.exists():
        qs.update(active = False)

pre_save.connect(pre_save_create_order_id, sender = Order)

def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created: #if the order changes and it's not being created, reference the cart and update the total of the cart
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id = cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()
post_save.connect(post_save_cart_total, sender = Cart)

def post_save_order(sender, instance, created, *args, **kwargs):
    if created: # whenever we make a new order, update total
        instance.update_total()
post_save.connect(post_save_order, sender=Order)
