# -*- coding: utf-8 -*-

from django.urls import re_path
from communication.views import display_search, logo_public_load, \
    logo_public_list, website_news, random_slide, ecrans

urlpatterns = [
    re_path(r'^ecrans$', ecrans, name='communication-views-ecrans'),
    re_path(r'^random_slide$', random_slide, name='communication-views-random_slide'),
    re_path(r'^website_news$', website_news, name='communication-views-website_news'),
    re_path(r'^logo_public_list$', logo_public_list, name='communication-views-logo_public_list'),
    re_path(r'^logo_public_load$', logo_public_load, name='communication-views-logo_public_load'),
    re_path('display/search', display_search, name='communication-views-display_search'),
]
