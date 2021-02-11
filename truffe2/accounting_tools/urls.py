# -*- coding: utf-8 -*-

from django.urls import re_path
from accounting_tools.views import cashbook_csv, expenseclaim_csv, \
    internaltransfer_csv, provider_invoice_pdf, export_demands_yearly, \
    export_all_demands, provider_available_list, \
    cashbook_pdf, expenseclaim_pdf, internaltransfer_pdf, get_withdrawal_infos, \
    withdrawal_available_list, withdrawal_pdf, invoice_bvr, invoice_pdf

urlpatterns = [
    re_path(r'^subvention/(?P<ypk>[0-9]+)/export$', export_demands_yearly, name='accounting_tools-views-export_demands_yearly'),
    re_path(r'^subvention/export_all$', export_all_demands, name='accounting_tools-views-export_all_demands'),

    re_path(r'^invoice/(?P<pk>[0-9]+)/pdf/', invoice_pdf, name='accounting_tools-views-invoice_pdf'),
    re_path(r'^invoice/(?P<pk>[0-9]+)/bvr/', invoice_bvr, name='accounting_tools-views-invoice_bvr'),

    re_path(r'^withdrawal/(?P<pk>[0-9]+)/pdf/', withdrawal_pdf, name='accounting_tools-views-withdrawal_pdf'),
    re_path(r'^withdrawal/list/', withdrawal_available_list, name='accounting_tools-views-withdrawal_available_list'),
    re_path(r'^withdrawal/(?P<pk>[0-9]+)/infos/', get_withdrawal_infos, name='accounting_tools-views-get_withdrawal_infos'),

    re_path(r'^internaltransfer/(?P<pk>[0-9,]+)/pdf/', internaltransfer_pdf, name='accounting_tools-views-internaltransfer_pdf'),
    re_path(r'^expenseclaim/(?P<pk>[0-9]+)/pdf/', expenseclaim_pdf, name='accounting_tools-views-expenseclaim_pdf'),
    re_path(r'^cashbook/(?P<pk>[0-9]+)/pdf/', cashbook_pdf, name='accounting_tools-views-cashbook_pdf'),

    re_path(r'^financialprovider/list/', provider_available_list, name='accounting_tools-views-provider_available_list'),
    re_path(r'^providerinvoice/(?P<pk>[0-9]+)/pdf/', provider_invoice_pdf, name='accounting_tools-views-provider_invoice_pdf'),
    
    re_path(r'^internaltransfer/(?P<pk>[0-9,]+)/csv/', internaltransfer_csv, name='accounting_tools-views-internaltransfer_csv'),
    re_path(r'^expenseclaim/(?P<pk>[0-9,]+)/csv/', expenseclaim_csv, name='accounting_tools-views-expenseclaim_csv'),
    re_path(r'^cashbook/(?P<pk>[0-9,]+)/csv/', cashbook_csv, name='accounting_tools-views-cashbook_csv'),
]
