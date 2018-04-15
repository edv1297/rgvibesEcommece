from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.static import serve

from accounts.views import login_page, register_page, guest_register_view
from addresses.views import checkout_address_create_view
from .views import (
    home,
    contact,
    about,
    catalog,

)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name= 'home'),
    url(r'^about/$', about, name = 'about'),
    url(r'^checkout/address/create', checkout_address_create_view, name ='checkout_address_create'),
    url(r'^contact/$', contact, name = 'contact'),
    url(r'^login/$', login_page, name = 'login'),
    url(r'^logout/$', LogoutView.as_view(), name = 'logout'),
    url(r'^register/$', register_page, name = 'register'),
    url(r'^register/guest$', guest_register_view, name = 'guest_register'),
    url(r'^products/', include("products.urls", namespace = 'products')), # namespace adds more specificity for each route
    url(r'^search/', include("search.urls", namespace = 'search')),
    url(r'^cart/', include("carts.urls", namespace = 'cart'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})]
