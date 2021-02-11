# -*- coding: utf-8 -*-

from django.urls import re_path
from logistics.views import loanagreement_pdf, supply_search, room_search

urlpatterns = [
     re_path('room/search', room_search, name='logistics-views-room_search'),
    re_path('supply/search', supply_search, name='logistics-views-supply_search'),
    re_path(r'^loanagreement/(?P<pk>[0-9]+)/pdf/', loanagreement_pdf, name='logistics-views-loanagreement_pdf'),
]
