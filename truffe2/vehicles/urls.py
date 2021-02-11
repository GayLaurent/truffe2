
# -*- coding: utf-8 -*-

from django.urls import re_path
from vehicles.views import booking_pdf

urlpatterns = [
    re_path(r'^booking/(?P<pk>[0-9]+)/pdf/', booking_pdf, name='vehicles-views-booking_pdf'),
]
