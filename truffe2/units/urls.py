# -*- coding: utf-8 -*-

from django.urls import re_path
from units.views import accreds_list, accreds_list_json, accreds_logs_list, \
    accreds_logs_list_json, accreds_renew, accreds_edit, accreds_delete, \
    accreds_validate, accreds_add, role_userslist

urlpatterns = [
    re_path(r'^accreds/$', accreds_list, name='units-views-accreds_list'),
    re_path(r'^accreds/json$', accreds_list_json, name='units-views-accreds_list_json'),
    re_path(r'^accreds/logs/$', accreds_logs_list, name='units-views-accreds_logs_list'),
    re_path(r'^accreds/logs/json$', accreds_logs_list_json, name='units-views-accreds_logs_list_json'),
    re_path(r'^accreds/(?P<pk>[0-9,]+)/renew$', accreds_renew, name='units-views-accreds_renew'),
    re_path(r'^accreds/(?P<pk>[0-9~]+)/edit$', accreds_edit, name='units-views-accreds_edit'),
    re_path(r'^accreds/(?P<pk>[0-9,]+)/delete$', accreds_delete, name='units-views-accreds_delete'),
    re_path(r'^accreds/(?P<pk>[0-9,]+)/validate$', accreds_validate, name='units-views-accreds_validate'),
    re_path(r'^accreds/add$', accreds_add, name='units-views-accreds_add'),
    re_path(r'^role/(?P<pk>\d*)/users$', role_userslist, name='units-views-role_userslist'),
]
