# -*- coding: utf-8 -*-

from django.urls import re_path
from django.contrib.auth.decorators import login_required

from main.views import HaystackSearchView, home, \
    get_to_moderate, link_base, \
    last_100_logging_entries, set_homepage, \
    file_download_list, \
    file_download, \
    signabledocument_download, \
    signabledocument_signs, signabledocument_sign

urlpatterns = [
    re_path(r'^$', home, name='main-views-home'),
    re_path(r'^get_to_moderate$', get_to_moderate, name='main-views-get_to_moderate'),

    re_path(r'^link/base$', link_base, name='main-views-link_base'),
    re_path(r'^last_100_logging_entries$', last_100_logging_entries, name='main-views-last_100_logging_entries'),

    re_path(r'^search/?$', login_required(HaystackSearchView()), name='search_view'),

    re_path(r'^set_homepage$', set_homepage, name='main-views-set_homepage'),

    re_path(r'^file/download_list/$', file_download_list, name='main-views-file_download_list'),
    re_path(r'^file/download/(?P<pk>[0-9,]+)$', file_download, name='main-views-file_download'),

    re_path(r'^signabledocument/download/(?P<pk>[0-9,]+)$', signabledocument_download, name='main-views-signabledocument_download'),
    re_path(r'^signabledocument/sign/(?P<pk>[0-9,]+)$', signabledocument_sign, name='main-views-signabledocument_sign'),
    re_path(r'^signabledocument/signs/$', signabledocument_signs, name='main-views-signabledocument_signs'),
]
