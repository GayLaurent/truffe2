# -*- coding: utf-8 -*-

from django.urls import re_path
from notifications.views import mark_as_read, \
    notification_restrictions_update, \
    dropdown, goto, \
    notification_center, \
    notification_keys, \
    notification_json, \
    notification_restrictions

urlpatterns = [
    re_path(r'^dropdown$', dropdown, name='notifications-views-dropdown'),
    re_path(r'^goto/(?P<pk>[0-9]+)$', goto, name='notifications-views-goto'),
    re_path(r'^center/$', notification_center, name='notifications-views-notification_center'),
    re_path(r'^center/keys$', notification_keys, name='notifications-views-notification_keys'),
    re_path(r'^center/json$', notification_json, name='notifications-views-notification_json'),
    re_path(r'^center/restrictions$', notification_restrictions, name='notifications-views-notification_restrictions'),
    re_path(r'^center/restrictions/update$', notification_restrictions_update, name='notifications-views-notification_restrictions_update'),
    re_path(r'^read$', mark_as_read, name='notifications-views-mark_as_read'),
]
