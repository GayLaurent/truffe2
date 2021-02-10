# -*- coding: utf-8 -*-
'''
Unit test tools for truffe

'''
from bs4 import BeautifulSoup
from json import loads
import os
import sys
from io import StringIO
from os.path import dirname, join, isdir, isfile

from django.test import TestCase, Client
from django.test.client import MULTIPART_CONTENT
from django.core.management import call_command

from main.test_data import setup_testing_all_data


class TruffeTestAbstract(TestCase, Client):
    
    login_username = None

    PDF_DIRECTORY = 'pdf'

    def __init__(self, methodName):
        TestCase.__init__(self, methodName)
        Client.__init__(self)
        self.send_content_type = MULTIPART_CONTENT

    def _get_pdf_filename(self):
        return join(self.PDF_DIRECTORY, "%s-%s-%s.pdf" % (self.__class__.__module__, self.__class__.__name__, self._testMethodName))

    def setUp(self):
        TestCase.setUp(self)
        setup_testing_all_data()
        if self.login_username is not None:
            self.connect_to(self.login_username)
        if not isdir(self.PDF_DIRECTORY):
            os.makedirs(self.PDF_DIRECTORY)
        filename = self._get_pdf_filename()
        if isfile(filename):
            os.unlink(filename)

    def connect_to(self, username):
        self.call_check_html('/users/login')
        csr_token_input = self.content.findAll('input', {'name': 'csrfmiddlewaretoken'})[0]           
        self.call_check_redirect('/users/login', {'username': username, 'password': username, 'csrfmiddlewaretoken': csr_token_input}, 'post', '/')
        self.call_check_html('/')
        
    def _decode_content(self):
        for encoding in ('utf-8', 'latin1', 'ascii', 'utf-16'):
            try:
                return self.response.content.decode(encoding)
            except UnicodeDecodeError:
                pass
        raise UnicodeDecodeError('not decode')

    def _get_default_content_type(self):
        if self.response.status_code != 200:
            return ""
        if b'<!DOCTYPE html>' in self.response.content:
            default_type = 'text/html'
        elif len(self.response.content) == 0:
            default_type = 'text/text'
        elif self.response.content[1:4] == b'PDF':
            default_type = 'application/pdf'
        elif self.response.content.strip()[:1] in (b'[', b'{'):
            default_type = 'application/json'
        else:
            from PIL import Image, UnidentifiedImageError
            try:
                from io import BytesIO
                img = Image.open(BytesIO(self.response.content))
                default_type = 'image/' + img.format.lower()
            except (ValueError, UnidentifiedImageError):
                try:
                    self._decode_content()
                    default_type = 'text/text'
                except UnicodeDecodeError:
                    default_type = 'application/octet-stream'
        return default_type

    def call(self, path, data={}, method='get', status_expected=200):
        self.response = getattr(self, method.lower(), self.get)(path, data, content_type=self.send_content_type)
        self.content_type = getattr(self.response, 'content_type', self._get_default_content_type())
        self.content = self.response.content
        if status_expected != 0:
            self.assertEqual(self.response.status_code, status_expected, "HTTP error [%s]:%s" % (self.response.status_code, self.get_div('text-center error-box', True)))

    def call_check_redirect(self, path, data={}, method='get', redirect_url=None, target_status_code=200):
        self.call(path, data, method, status_expected=302)
        self.assertRedirects(self.response, '/users/login?next=%s' % path if redirect_url is None else redirect_url, target_status_code=target_status_code)        

    def _check_alert(self, alert_expected):
        alert_dom = []
        for div_dom in self.content.findAll('div', {'class': 'alert alert-danger'}):
            if (div_dom.has_attr('style') and ('display: none;' in div_dom['style'])) or (div_dom.parent.has_attr('style') and ('display: none;' in div_dom.parent['style'])):
                continue 
            alert_dom.append(div_dom.text.strip())
        self.assertEqual('\n'.join(alert_dom), alert_expected)

    def _check_formerror(self, formerror_expected):

        def extract_names(divitem):
            names = []
            if divitem is not None:
                for sub_item in divitem:
                    if 'name' in sub_item:
                        names.append(sub_item['name'])
                    if sub_item.name == 'div':
                        names.extend(extract_names(sub_item))
            return names

        form_error = []
        form_error_dom = self.content.findAll('div', {'class':'form-group has-error'})
        for form_error_item in form_error_dom:
            form_error.extend(extract_names(form_error_item.div))
        self.assertListEqual(form_error, formerror_expected)

    def _check_warning(self, warning_expected):

        def extract_title(smallbox_text):
            titles = []
            for smallbox_item in smallbox_text.split('\n'):
                smallbox_item = smallbox_item.strip()
                if smallbox_item.startswith('title'):
                    titles.append(':'.join(smallbox_item.split(':')[1:]).strip()[1:-2])
            return titles

        warning_list = []
        smallbox_text = self._decode_content()
        smallbox_pos = smallbox_text.find('$.smallBox({')
        while smallbox_pos != -1:
            end_pos = smallbox_text.find('}', smallbox_pos + 12)
            warning_list.extend(extract_title(smallbox_text[smallbox_pos + 12:end_pos]))
            smallbox_text = smallbox_text[end_pos + 1]
            smallbox_pos = smallbox_text.find('$.smallBox({')
        self.assertEqual("\n".join(warning_list), warning_expected)

    def _convert_html(self):
        try:
            self.content = BeautifulSoup(self.response.content, "html.parser")
        except Exception:
            self.content = self.response.content

    def call_check_html(self, path, data={}, method='get', alert_expected='', warning_expected='', formerror_expected=[]):
        self.call(path, data, method)
        self._convert_html()
        self.assertEqual(self.content_type, "text/html")
        self._check_alert(alert_expected)
        self._check_formerror(formerror_expected)
        self._check_warning(warning_expected)

    def call_check_json(self, path, data={}, method='get'):
        self.call(path, data, method)
        self.assertEqual(self.content_type, "application/json")
        self.content = loads(self.response.content.decode('utf-8'))

    def call_check_pdf(self, path, data={}, method='get'):
        self.call(path, data, method)
        self.assertEqual(self.content_type, "application/pdf")
        filename = self._get_pdf_filename()
        with open(filename, "wb") as pdf_writer:
            pdf_writer.write(self.response.content)

    def call_check_text(self, path, data={}, method='get', alert_expected='', warning_expected='', formerror_expected=[]):
        self.call(path, data, method)
        self.assertEqual(self.content_type, "text/text")
        self._convert_html()
        self._check_warning(warning_expected)
        if isinstance(self.content, BeautifulSoup):
            self._check_formerror(formerror_expected)
            self._check_alert(alert_expected)

    def get_div(self, class_to_find, return_all=False):
        try:
            if not isinstance(self.content, BeautifulSoup):
                self._convert_html()
            div_dom = self.content.findAll('div', {'class': class_to_find})
            return "\n".join([item.text.strip() for item in div_dom])
        except Exception:
            return self.content if return_all else None


class TruffeCmdTestAbstract(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        setup_testing_all_data()
        self.old_stdin = sys.stdin
        os.chdir(dirname(dirname(__file__)))
        self.fileout = StringIO()
        self.fileerr = StringIO()
        self.filein = StringIO()
        sys.stdin = self.filein
        
    def tearDown(self):
        TestCase.tearDown(self)
        sys.stdin = self.old_stdin 
        self.fileout.close()
        self.fileerr.close()
        self.filein.close()
    
    def call_command(self, *args, **kwargs):
        command_name = self._testMethodName[5:]
        while command_name[-1] in (str(val) for val in range(10)):
            command_name = command_name[:-1]
        self.filein.seek(0)
        return call_command(command_name, *args, stdout=self.fileout, stderr=self.fileout, **kwargs)
