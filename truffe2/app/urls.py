
import django.views.static
from django.urls import include, re_path
from django.conf import settings

urlpatterns = [
    re_path(r'', include('main.urls')),
    re_path(r'^accounting/core/', include('accounting_core.urls')),
    re_path(r'^accounting/tools/', include('accounting_tools.urls')),
    re_path(r'^accounting/main/', include('accounting_main.urls')),
    re_path(r'^users/', include('users.urls')),
    re_path(r'^members/', include('members.urls')),
    re_path(r'^units/', include('units.urls')),
    re_path(r'^communication/', include('communication.urls')),
    re_path(r'^notifications/', include('notifications.urls')),
    re_path(r'^logistics/', include('logistics.urls')),
    re_path(r'^vehicles/', include('vehicles.urls')),
    re_path(r'^generic/', include('generic.urls')),

    re_path(r'^impersonate/', include('impersonate.urls')),

    re_path(r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),  # In prod, use apache !
    re_path(r'^' + settings.STATIC_URL[1:] + '(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),  # In prod, use apache !
]
