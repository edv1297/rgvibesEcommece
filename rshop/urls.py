from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve


from .views import (
    home,
    contact,
    about,
    catalog,
    login_page,
    register_page
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name= 'home'),
    url(r'^about/$', about, name = 'about'),
    url(r'^contact/$', contact, name = 'contact'),
    url(r'^login/$', login_page, name = 'login'),
    url(r'^register/$', register_page, name = 'register'),
    url(r'^products/', include("products.urls", namespace = 'products')), # namespace adds more specificity for each route
    url(r'^search/', include("search.urls", namespace = 'search')),
    url(r'^cart/', include("carts.urls", namespace = 'cart'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})]
