# -*- coding: utf-8 -*-

from django.urls import include, re_path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    LogoutView

from users.views import users_myunit_pdf, users_myunit_vcard, \
    users_profile_picture, \
    password_change_done, password_change_check, users_create_external, \
    users_set_body, users_list, users_list_json, users_profile, \
    users_vcard, users_edit, users_myunit_list, login, users_myunit_list_json, \
    ldap_search
import app.tequila

urlpatterns = [
    re_path(r'^login$', login, name='users-views-login'),
    re_path(r'^login_done$', login, {'why': 'reset_done'}, name='login_with_rst_done'),
    re_path(r'^login_cptd$', login, {'why': 'reset_completed'}, name='login_with_rst_completed'),
    re_path(r'^create_external$', users_create_external, name='users-views-users_create_external'),
    re_path(r'password_change_check', password_change_check, name='users-views-password_change_check'),
    re_path(r'password_change/done/$', password_change_done, name='password_change_done'),
    re_path(r'^password_reset/$', PasswordResetView.as_view(), {'post_reset_redirect': 'login_with_rst_done',
        'from_email': 'nobody@truffe.agepoly.ch',
        'html_email_template_name': '/registration/password_reset_email_html.html'}, name='password_reset'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), {'post_reset_redirect': 'login_with_rst_completed'}, name='password_reset_completed'),
    re_path(r'^', include('django.contrib.auth.urls')),

    re_path(r'^set_body/(?P<mode>[mh\_])$', users_set_body, name='users-views-users_set_body'),
    re_path(r'^users/$', users_list, name='users-views-users_list'),
    re_path(r'^users/json$', users_list_json, name='users-views-users_list_json'),
    re_path(r'^users/(?P<pk>[0-9~]+)$', users_profile, name='users-views-users_profile'),
    re_path(r'^users/(?P<pk>[0-9~]+)/vcard$', users_vcard, name='users-views-users_vcard'),
    re_path(r'^users/(?P<pk>[0-9~]+)/edit$', users_edit, name='users-views-users_edit'),
    re_path(r'^users/(?P<pk>[0-9~]+)/profile_picture$', users_profile_picture, name='users-views-users_profile_picture'),

    re_path(r'^myunit/$', users_myunit_list, name='users-views-users_myunit_list'),
    re_path(r'^myunit/json$', users_myunit_list_json, name='users-views-users_myunit_list_json'),
    re_path(r'^myunit/vcard$', users_myunit_vcard, name='users-views-users_myunit_vcard'),
    re_path(r'^myunit/pdf/$', users_myunit_pdf, name='users-views-users_myunit_pdf'),

    re_path(r'^ldap/search$', ldap_search, name='users-views-ldap_search'),
    re_path(r'^logout$', LogoutView.as_view(next_page='/'), name='django-contrib-auth-views-logout'),
]

urlpatterns.append(re_path(r'^login/tequila$', app.tequila.login, name='app-tequila-login'))
