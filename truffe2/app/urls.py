
import django.views.static
from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
    url(r'', include('main.urls')),
    url(r'^accounting/core/', include('accounting_core.urls')),
    url(r'^accounting/tools/', include('accounting_tools.urls')),
    url(r'^accounting/main/', include('accounting_main.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^units/', include('units.urls')),
    url(r'^communication/', include('communication.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^logistics/', include('logistics.urls')),
    url(r'^vehicles/', include('vehicles.urls')),
    url(r'^generic/', include('generic.urls')),

    url(r'^impersonate/', include('impersonate.urls')),

    url(r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),  # In prod, use apache !
    url(r'^' + settings.STATIC_URL[1:] + '(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),  # In prod, use apache !
]
