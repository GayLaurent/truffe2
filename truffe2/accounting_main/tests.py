# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from re import match

from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from main.test_tools import TruffeTestAbstract


class AccountingMainNoLoginTest(TruffeTestAbstract):
    
    def test_accounting_graph(self):
        self.call_check_redirect('/accounting/main/accounting/graph/')

    def test_accounting_errors_send_message(self):
        self.call_check_redirect('/accounting/main/accounting/errors/send_message/1')

    def test_accounting_import_step0(self):
        # TODO : no '@login_required' for this view
        self.call('/accounting/main/accounting/import/step/0', status_expected=404)

    def test_accounting_import_step1(self):
        self.call_check_redirect('/accounting/main/accounting/import/step/1/1')

    def test_accounting_import_step2(self):
        self.call_check_redirect('/accounting/main/accounting/import/step/2/1')

    def test_budget_available_list(self):
        self.call_check_redirect('/accounting/main/budget/available_list'),

    def test_budget_copy(self):        self.call_check_redirect('/accounting/main/budget/1/copy')

    def test_budget_get_infos(self):
        self.call_check_redirect('/accounting/main/budget/1/get_infos')

    def test_budget_pdf(self):
        self.call_check_redirect('/accounting/main/budget/1/pdf/'),

    def test_accounting_budget_view(self):
        self.call_check_redirect('/accounting/main/accounting/budget_view'),

    def test_budget_list(self):
        self.call_check_redirect('/accounting/main/budget/')

    def test_budget_mayi(self):
        self.call_check_redirect('/accounting/main/budget/mayi')

    def test_budget_json(self):
        self.call_check_redirect('/accounting/main/budget/json')

    def test_budget_deleted(self):
        self.call_check_redirect('/accounting/main/budget/deleted')

    def test_budget_logs(self):
        self.call_check_redirect('/accounting/main/budget/logs')

    def test_budget_logs_json(self):
        self.call_check_redirect('/accounting/main/budget/logs/json')

    def test_budget_add(self):
        self.call_check_redirect('/accounting/main/budget/~/edit')

    def test_budget_edit(self):
        self.call_check_redirect('/accounting/main/budget/1/edit')

    def test_budget_delete(self):
        self.call_check_redirect('/accounting/main/budget/1/delete')

    def test_budget_show(self):
        self.call_check_redirect('/accounting/main/budget/1/')

    def test_budget_switch_status(self):
        self.call_check_redirect('/accounting/main/budget/1/switch_status')

    def test_budget_contact(self):
        self.call_check_redirect('/accounting/main/budget/1/contact/canedit')
         
    def test_accountingline_list(self):
        self.call_check_redirect('/accounting/main/accountingline/')

    def test_accountingline_mayi(self):
        self.call_check_redirect('/accounting/main/accountingline/mayi')

    def test_accountingline_json(self):
        self.call_check_redirect('/accounting/main/accountingline/json')

    def test_accountingline_deleted(self):
        self.call_check_redirect('/accounting/main/accountingline/deleted')

    def test_accountingline_logs(self):
        self.call_check_redirect('/accounting/main/accountingline/logs')

    def test_accountingline_logs_json(self):
        self.call_check_redirect('/accounting/main/accountingline/logs/json')

    def test_accountingline_edit(self):
        self.call_check_redirect('/accounting/main/accountingline/2/edit')

    def test_accountingline_delete(self):
        self.call_check_redirect('/accounting/main/accountingline/2/delete')

    def test_accountingline_show(self):
        self.call_check_redirect('/accounting/main/accountingline/2/')

    def test_accountingline_switch_status(self):
        self.call_check_redirect('/accounting/main/accountingline/2/switch_status')

    def test_accountingline_contact(self):
        self.call_check_redirect('/accounting/main/accountingline/2/contact/editor') 


class AccountingMainWithLoginTest(TruffeTestAbstract):
    
    login_username = 'admin'
    
    def test_accounting_graph(self):
        self.call_check_text('/accounting/main/accounting/graph/', data={'costcenter':1})

    def test_accounting_errors_send_message(self):
        self.call_check_text('/accounting/main/accounting/errors/send_message/1', method='post', data={'message':'abc 123'})

    def test_accounting_import_step0(self):
        self.call('/accounting/main/accounting/import/step/0', status_expected=302)
        url_splited = self.response.url.split('/')
        self.assertEqual('/'.join(url_splited[:-1]), '/accounting/main/accounting/import/step/1', self.response.url)
        self.assertTrue(match(r'[a-z0-9\-]+', url_splited[-1]), self.response.url)

    def test_accounting_import_step1(self):
        now = timezone.now()
        content_csv = """Extrait CdC
Extrait de:  01.01.YYYY  bis  31.12.YYYY
Tous CdC

CdC
Date\tPi\xe8ce\tTexte d'\xe9criture\tType C.\tD\xe9bit CHF\tCr\xe9dit CHF\tCourant 
Solde CHF\t
1234  center\t\t\t\t\t\t\t
01.08.YYYY\t376\tSolde au 01.08.YYYY\t2850\t\t238'950.81\t238'950.81\t-
22.08.YYYY\t10\tFacture CH-0078-YYYY-1, ass. accidents pour les staffs - 21291 Assurances SA\t6340\t1'243.40\t\t237'707.41\t-
22.08.YYYY\t11\tFacture abo annuel du 01.08.YYYY au 31.07.2020 - 20393 Sage suisse SA\t6550\t1'387.60\t\t236'319.81\t-
22.08.YYYY\t12\tFacture n°1000666369, inscription au RC - 20276 Etat de Vaud , Ordre judiciaire \t6560\t820.00\t\t235'499.81\t-
22.08.YYYY\t12\tFacture n°1000666369, inscription au RC - 20276 Etat de Vaud , Ordre judiciaire \t6560\t27.86\t\t235'471.95\t-
22.08.YYYY\t16\tFacture n°791961028, location photocopieuse 08.YYYY - 20023 Canon (Schweiz) AG \t6410\t230.00\t\t235'241.95\t-
22.08.YYYY\t17\tFacture n°401237743 , location 08.YYYY- 20023 Canon (Schweiz) AG \t6410\t80.00\t\t235'161.95\t-
23.08.YYYY\t425\tPmt salaire 08.YYYY, Z. CUFU\t2229\t2'287.30\t\t232'874.65\t-
23.08.YYYY\t426\tPmt salaire 08.YYYY, O. QUGIBI\t2229\t3'521.40\t\t229'353.25\t-
23.08.YYYY\t427\tPmt salaire 08.YYYY, M. VATU\t2229\t5'406.60\t\t223'946.65\t-
30.08.YYYY\t437\tFrais trafic des paiements au 31.08.YYYY\t6710\t25.10\t\t223'921.55\t-
"""
        file_to_upload = SimpleUploadedFile("accounting.csv", content_csv.replace('YYYY', str(now.year)).encode(), content_type="text/plain")
        sess = self.session
        sess.update({'T2_ACCOUNTING_IMPORT_def-123-abc': {'is_valid': True, 'has_data': False}})
        sess.save()
        self.call_check_html('/accounting/main/accounting/import/step/1/def-123-abc')
        self.call_check_html('/accounting/main/accounting/import/step/1/def-123-abc?send=notif', method='post', warning_expected="Notification envoyée !")
        self.call_check_redirect('/accounting/main/accounting/import/step/1/def-123-abc', data={'year':1, 'file':file_to_upload, 'type':'tab_2016'},
                             method='post', redirect_url='/accounting/main/accounting/import/step/2/def-123-abc')

    def test_accounting_import_step2(self):
        sess = self.session
        sess.update({'T2_ACCOUNTING_IMPORT_def-123-abc': {'is_valid': True, 'has_data': True, 'year':1,
                                                          'data': {'nop':[],
                                                                   'to_delete':[],
                                                                   'to_update':[],
                                                                   'to_add': [{'current_sum':-238950.81, 'account': u'2850', 'input': '238950.81', 'costcenter': u'1234', 'output': '0.0', 'date': '2020-08-01', 'text': u'Solde au 01.08.2020', 'tva': '0.0', 'order': 0, 'document_id': u'376'},
                                                                              {'current_sum':-237707.41, 'account': u'6340', 'input': '0.0', 'costcenter': u'1234', 'output': '1243.4', 'date': '2020-08-22', 'text': u'Facture CH-0078-2020-1, ass. accidents pour les staffs - 21291 Assurances SA', 'tva': '0.0', 'order': 1, 'document_id': u'10'},
                                                                              {'current_sum':-236319.81, 'account': u'6550', 'input': '0.0', 'costcenter': u'1234', 'output': '1387.6', 'date': '2020-08-22', 'text': u'Facture abo annuel du 01.08.2020 au 31.07.2020 - 20393 Sage suisse SA', 'tva': '0.0', 'order': 2, 'document_id': u'11'}]        
                                                                    }}})
        sess.save()
        self.call_check_html('/accounting/main/accounting/import/step/2/def-123-abc')
        self.call_check_redirect('/accounting/main/accounting/import/step/2/def-123-abc',
                                 method='post', redirect_url='/accounting/main/accounting/import/step/0', target_status_code=302)

    def test_budget_available_list(self):
        self.call_check_json('/accounting/main/budget/available_list', data={'upk':1, 'ypk':1}),

    def test_budget_copy(self):
        self.call_check_redirect('/accounting/main/budget/1/copy', redirect_url='/accounting/main/budget/2/edit')

    def test_budget_get_infos(self):
        self.call_check_json('/accounting/main/budget/1/get_infos')

    def test_budget_pdf(self):
        self.call_check_pdf('/accounting/main/budget/1/pdf/')

    def test_accounting_budget_view(self):
        self.call_check_text('/accounting/main/accounting/budget_view', data={'costcenter':1})

        self.call_check_text('/accounting/main/accounting/budget_view?costcenter=1', data={}, method='post')

    def test_budget_list(self):
        self.call_check_html('/accounting/main/budget/')

    def test_budget_mayi(self):
        self.call_check_json('/accounting/main/budget/mayi')

    def test_budget_json(self):
        self.call_check_json('/accounting/main/budget/json')

    def test_budget_deleted(self):
        from accounting_main.models import Budget
        Budget(id=2, name='bad budget', unit_id=1, accounting_year_id=1, costcenter_id=1, deleted=True).save()        
        self.call_check_html('/accounting/main/budget/deleted', data={'upk':1})
        self.call_check_redirect('/accounting/main/budget/deleted', method='post', data={'upk':1, 'pk':2}, redirect_url='/accounting/main/budget/')

    def test_budget_logs(self):
        self.call_check_html('/accounting/main/budget/logs')

    def test_budget_logs_json(self):
        self.call_check_json('/accounting/main/budget/logs/json')

    def test_budget_add(self):
        self.call_check_html('/accounting/main/budget/~/edit', data={'upk':1, 'ypk':1})
        self.call_check_redirect('/accounting/main/budget/~/edit', method='post',
                             data={'upk':1, 'ypk':1, 'tags':'', 'name':'my budget', 'costcenter':1}, redirect_url='/accounting/main/budget/2/')

    def test_budget_edit(self):
        self.call_check_html('/accounting/main/budget/1/edit')
        self.call_check_redirect('/accounting/main/budget/1/edit', method='post',
                                 data={'tags':'', 'name':'new budget', 'costcenter':1}, redirect_url='/accounting/main/budget/1/')

    def test_budget_delete(self):
        self.call_check_html('/accounting/main/budget/1/delete')

    def test_budget_show(self):
        self.call_check_html('/accounting/main/budget/1/')

    def test_budget_switch_status(self):
        self.call_check_text('/accounting/main/budget/1/switch_status', data={'dest_status':'2_treated', 'from_list':'from_list'})
        self.call_check_text('/accounting/main/budget/1/switch_status?dest_status=2_treated&from_list=from_list', method='post', data={'do':'it'})
        self.assertIn('window.location.reload();', self.response.content.decode('utf-8'))

    def test_budget_contact(self):
        self.call_check_text('/accounting/main/budget/1/contact/agep_compta') 
        self.call_check_text('/accounting/main/budget/1/contact/agep_compta', method='post', data={'key':'agep_compta', 'subject':'ask', 'message':'blabla', 'receive_copy':True}) 

    def test_accountingline_list(self):
        self.call_check_html('/accounting/main/accountingline/', data={'iSortingCols':2, 'iSortCol_0':1, 'iSortCol_1':3, 'iDisplayLength':5, 'iDisplayStart':0, 'sSearch': 'account'})

    def test_accountingline_mayi(self):
        self.call_check_json('/accounting/main/accountingline/mayi')

    def test_accountingline_json(self):
        self.call_check_json('/accounting/main/accountingline/json')

    def test_accountingline_deleted(self):
        from accounting_main.models import AccountingLine
        now = timezone.now()
        AccountingLine(id=20, account_id=1, date=now, tva=0.0, text='line bad', output=11.11, input=0.0, current_sum=0.0, order=1, accounting_year_id=1, costcenter_id=1, deleted=True).save()
        self.call_check_html('/accounting/main/accountingline/deleted', data={'upk':1})
        self.call_check_redirect('/accounting/main/accountingline/deleted', method='post', data={'upk':1, 'pk':20}, redirect_url='/accounting/main/accountingline/')

    def test_accountingline_logs(self):
        self.call_check_html('/accounting/main/accountingline/logs')

    def test_accountingline_logs_json(self):
        self.call_check_json('/accounting/main/accountingline/logs/json')

    def test_accountingline_add(self):
        self.call_check_html('/accounting/main/accountingline/~/edit', data={'upk':1, 'ypk':1})
        self.call_check_redirect('/accounting/main/accountingline/~/edit', method='post',
                             data={'upk':1, 'ypk':1, 'date':'2020-01-01', 'tva':0.0, 'text':'aaa', 'output':1.23, 'input':2.34, 'current_sum':4.56, 'order':2, 'costcenter':1, 'account':4},
                             redirect_url='/accounting/main/accountingline/10/')

    def test_accountingline_edit(self):
        self.call_check_html('/accounting/main/accountingline/2/edit')
        self.call_check_redirect('/accounting/main/accountingline/2/edit', method='post',
                             data={'date':'2020-01-01', 'tva':0.0, 'text':'aaa', 'output':1.23, 'input':2.34, 'current_sum':4.56, 'order':2, 'costcenter':1, 'account':4},
                             redirect_url='/accounting/main/accountingline/2/')

    def test_accountingline_delete(self):
        self.call_check_html('/accounting/main/accountingline/2/delete')

    def test_accountingline_show(self):
        self.call_check_html('/accounting/main/accountingline/2/')

    def test_accountingline_switch_status(self):
        self.call_check_text('/accounting/main/accountingline/2/switch_status', data={'dest_status':'1_validated', 'from_list':'from_list'})
        self.call_check_text('/accounting/main/accountingline/2/switch_status?dest_status=1_validated&from_list=from_list', method='post', data={'do':'it'})
        self.assertIn('window.location.reload();', self.response.content.decode('utf-8'))

    def test_accountingline_contact(self):
        self.call_check_text('/accounting/main/accountingline/2/contact/editor') 
        self.call_check_text('/accounting/main/accountingline/2/contact/editor', method='post', data={'key':'editor', 'subject':'ask', 'message':'blabla', 'receive_copy':True})
