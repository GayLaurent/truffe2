# -*- coding: utf-8 -*-

from django.urls import re_path
from generic.views import check_unit_name

urlpatterns = [
    re_path('check_unit_name', check_unit_name, name='generic-views-check_unit_name'),
]
