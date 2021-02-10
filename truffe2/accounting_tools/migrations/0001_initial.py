# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounting_core.models
import generic.models
import generic.search
import rights.utils
import accounting_core.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('units', '__first__'),
        ('accounting_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Titre du journal de caisse')),
                ('nb_proofs', models.PositiveIntegerField(default=0, verbose_name='Nombre de justificatifs')),
                ('comment', models.TextField(null=True, verbose_name='Commentaire', blank=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'6_canceled', 'Annul\xe9'), (b'3_agep_sig2', 'Attente signature CdD 2'), (b'6_archived', 'Archiv\xe9'), (b'3_agep_sig1', 'Attente signature CdD 1'), (b'2_agep_validable', 'Attente v\xe9rification secr\xe9tariat'), (b'0_correct', 'Corrections n\xe9cessaires'), (b'0_draft', 'Brouillon'), (b'5_in_accounting', 'En comptabilisation'), (b'1_unit_validable', 'Attente accord unit\xe9'), (b'4_accountable', 'A comptabiliser')])),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True, on_delete=models.deletion.SET_NULL)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericTaggableObject, generic.models.GenericAccountingStateModel, generic.models.GenericStateModel, generic.models.GenericModelWithFiles, generic.models.GenericModelWithLines, accounting_core.utils.AccountingYearLinked, accounting_core.utils.CostCenterLinked, rights.utils.UnitEditableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.LinkedInfoModel, accounting_core.models.AccountingGroupModels, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='CashBookFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'uploads/_generic/CashBook/')),
                ('object', models.ForeignKey(related_name='files', blank=True, to='accounting_tools.CashBook', null=True, on_delete=models.deletion.SET_NULL)),
                ('uploader', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CashBookLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('date', models.DateField(verbose_name='Date')),
                ('helper', models.CharField(max_length=15, choices=[(b'0_withdraw', "J'ai fait un retrait cash : "), (b'1_deposit', "J'ai fait un versement \xe0 la banque : "), (b'2_sell', "J'ai vendu quelque chose : "), (b'3_invoice', "J'ai pay\xe9 une facture avec la caisse : "), (b'4_buy', "J'ai achet\xe9 quelque chose avec la caisse : "), (b'5_reimburse', "J'ai rembours\xe9 quelqu'un avec la caisse : "), (b'6_input', 'Je fais un Cr\xe9dit manuel : '), (b'7_output', 'Je fais un D\xe9bit manuel : ')])),
                ('label', models.CharField(max_length=255, verbose_name='Concerne')),
                ('proof', models.CharField(max_length=255, verbose_name='Justificatif', blank=True)),
                ('value', models.DecimalField(verbose_name='Montant (HT)', max_digits=20, decimal_places=2)),
                ('tva', models.DecimalField(verbose_name='VAT', max_digits=20, decimal_places=2)),
                ('value_ttc', models.DecimalField(verbose_name='Montant (TTC)', max_digits=20, decimal_places=2)),
                ('account', models.ForeignKey(verbose_name='Account', to='accounting_core.Account', on_delete=models.deletion.CASCADE)),
                ('cashbook', models.ForeignKey(related_name='lines', to='accounting_tools.CashBook', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CashBookLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.CashBook', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CashBookTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('object', models.ForeignKey(related_name='tags', to='accounting_tools.CashBook', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CashBookViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.CashBook', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpenseClaim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Titre de la note de frais')),
                ('nb_proofs', models.PositiveIntegerField(default=0, verbose_name='Nombre de justificatifs')),
                ('comment', models.TextField(null=True, verbose_name='Commentaire', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'6_canceled', 'Annul\xe9'), (b'3_agep_sig2', 'Attente signature CdD 2'), (b'6_archived', 'Archiv\xe9'), (b'3_agep_sig1', 'Attente signature CdD 1'), (b'2_agep_validable', 'Attente v\xe9rification secr\xe9tariat'), (b'0_correct', 'Corrections n\xe9cessaires'), (b'0_draft', 'Brouillon'), (b'5_in_accounting', 'En comptabilisation'), (b'1_unit_validable', 'Attente accord unit\xe9'), (b'4_accountable', 'A comptabiliser')])),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericTaggableObject, generic.models.GenericAccountingStateModel, generic.models.GenericStateModel, generic.models.GenericModelWithFiles, generic.models.GenericModelWithLines, accounting_core.utils.AccountingYearLinked, accounting_core.utils.CostCenterLinked, rights.utils.UnitEditableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.LinkedInfoModel, accounting_core.models.AccountingGroupModels, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='ExpenseClaimFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'uploads/_generic/ExpenseClaim/')),
                ('object', models.ForeignKey(related_name='files', blank=True, to='accounting_tools.ExpenseClaim', null=True, on_delete=models.deletion.SET_NULL)),
                ('uploader', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpenseClaimLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('label', models.CharField(max_length=255, verbose_name='Concerne')),
                ('proof', models.CharField(max_length=255, verbose_name='Justificatif', blank=True)),
                ('value', models.DecimalField(verbose_name='Montant (HT)', max_digits=20, decimal_places=2)),
                ('tva', models.DecimalField(verbose_name='VAT', max_digits=20, decimal_places=2)),
                ('value_ttc', models.DecimalField(verbose_name='Montant (TTC)', max_digits=20, decimal_places=2)),
                ('account', models.ForeignKey(verbose_name='Account', to='accounting_core.Account', on_delete=models.deletion.CASCADE)),
                ('expense_claim', models.ForeignKey(related_name='lines', to='accounting_tools.ExpenseClaim', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpenseClaimLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.ExpenseClaim', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpenseClaimTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('object', models.ForeignKey(related_name='tags', to='accounting_tools.ExpenseClaim', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpenseClaimViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.ExpenseClaim', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinancialProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom du fournisseur')),
                ('tva_number', models.CharField(help_text='CHE-XXX.XXX.XXX (<a href="https://www.uid.admin.ch/Search.aspx?lang=fr">Recherche</a>)', max_length=255, verbose_name='Num\xe9ro de TVA du fournisseur', blank=True)),
                ('iban_ou_ccp', models.CharField(help_text='(<a href="https://www.six-group.com/fr/products-services/banking-services/interbank-clearing/online-services/inquiry-iban.html">Convertir un num\xe9ro de compte en IBAN</a>) </br> Si la convertion ne fonctionne pas, noter CH00 et mettre le num\xe9ro de compte en remarque.', max_length=128, verbose_name='IBAN')),
                ('bic', models.CharField(help_text='Obligatoire si le fournisseur est \xe9tranger', max_length=128, verbose_name='BIC/SWIFT', blank=True)),
                ('address', models.CharField(help_text="Exemple: 'Rue Des Arc en Ciel 25 - Case Postale 2, CH-1015 Lausanne'", max_length=255, verbose_name='Adresse')),
                ('remarks', models.TextField(null=True, verbose_name='Remarques', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.search.SearchableModel, rights.utils.AgepolyEditableModel),
        ),
        migrations.CreateModel(
            name='FinancialProviderLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.FinancialProvider', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinancialProviderViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.FinancialProvider', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InternalTransfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Raison du transfert')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('amount', models.DecimalField(verbose_name='Montant', max_digits=20, decimal_places=2)),
                ('transfert_date', models.DateField(null=True, verbose_name='Date effective', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'1_agep_validable', 'Attente accord AGEPoly'), (b'3_canceled', 'Annul\xe9'), (b'0_draft', 'Brouillon'), (b'2_accountable', 'A comptabiliser'), (b'3_archived', 'Archiv\xe9')])),
                ('account', models.ForeignKey(verbose_name='Compte concern\xe9', to='accounting_core.Account', on_delete=models.deletion.CASCADE)),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('cost_center_from', models.ForeignKey(related_name='internal_transfer_from', verbose_name='Centre de co\xfbts pr\xe9lev\xe9', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
                ('cost_center_to', models.ForeignKey(related_name='internal_transfer_to', verbose_name='Centre de co\xfbts vers\xe9', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, generic.models.GenericTaggableObject, accounting_core.utils.AccountingYearLinked, rights.utils.AgepolyEditableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='InternalTransferLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.InternalTransfer', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InternalTransferTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('object', models.ForeignKey(related_name='tags', to='accounting_tools.InternalTransfer', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InternalTransferViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.InternalTransfer', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('custom_bvr_number', models.CharField(help_text='Ne PAS utiliser un num\xe9ro al\xe9atoire, mais utiliser un VRAI et UNIQUE num\xe9ro de BVR. Seulement pour des BVR physiques. Si pas renseign\xe9, un num\xe9ro sera g\xe9n\xe9r\xe9 automatiquement. Il est possible de demander des BVR \xe0 Marianne.', max_length=59, null=True, verbose_name='Num\xe9ro de BVR manuel', blank=True)),
                ('address', models.TextField(help_text="Exemple: 'Monsieur Poney - Rue Des Canard 19 - 1015 Lausanne'", null=True, verbose_name='Adresse', blank=True)),
                ('date_and_place', models.CharField(max_length=512, null=True, verbose_name='Lieu et date', blank=True)),
                ('preface', models.TextField(help_text="Texte affich\xe9 avant la liste. Exemple: 'Pour l'achat du Yearbook 2014' ou 'Ch\xe8re Madame, - Par la pr\xe9sente, je me permets de vous remettre notre facture pour le financement de nos activit\xe9s associatives pour l'ann\xe9e acad\xe9mique 2014-2015.'", null=True, verbose_name='Introduction', blank=True)),
                ('ending', models.TextField(help_text='Affich\xe9 apr\xe8s la liste, avant les moyens de paiements', max_length=1024, null=True, verbose_name='Conclusion', blank=True)),
                ('display_bvr', models.BooleanField(default=True, help_text="Affiche un BVR et le texte corespondant dans le PDF. Attention, le BVR g\xe9n\xe9r\xe9 n'est pas utilisable \xe0 la poste ! (Il est possible d'obtenir un 'vrai' BVR via Marianne.)", verbose_name='Afficher paiement via BVR')),
                ('display_account', models.BooleanField(default=True, help_text="Affiche le texte pour le paiement via le compte de l'AGEPoly.", verbose_name='Afficher paiement via compte')),
                ('greetings', models.CharField(default=b'', max_length=1024, null=True, verbose_name='Salutations', blank=True)),
                ('sign', models.TextField(help_text='Titre de la zone de signature', null=True, verbose_name='Signature', blank=True)),
                ('annex', models.BooleanField(default=False, help_text="Affiche 'Annexe(s): ment.' en bas de la facture", verbose_name='Annexes')),
                ('delay', models.SmallIntegerField(default=30, help_text="Mettre z\xe9ro pour cacher le texte. Il s'agit du nombre de jours de d\xe9lai pour le paiement.", verbose_name='D\xe9lai de paiement en jours')),
                ('english', models.BooleanField(default=False, help_text='G\xe9n\xe9re la facture en anglais', verbose_name='Anglais')),
                ('reception_date', models.DateField(help_text='Date de la r\xe9ception du paiement au niveau de la banque', null=True, verbose_name='Date valeur banque', blank=True)),
                ('add_to', models.BooleanField(default=False, verbose_name='Add "To the attention of"')),
                ('status', models.CharField(default=b'0_preparing', max_length=255, choices=[(b'1_need_bvr', "En attente d'un num\xe9ro BVR"), (b'5_canceled', 'Annul\xe9e'), (b'3_sent', 'Envoy\xe9e / paiement en attente'), (b'0_preparing', 'En pr\xe9paration'), (b'0_correct', 'Corrections n\xe9cessaires'), (b'2_ask_accord', 'Attente Accord AGEPoly'), (b'2_accord', 'Attente Envoi'), (b'4_archived', 'Archiv\xe9e / Paiement re\xe7u')])),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, generic.models.GenericTaggableObject, accounting_core.utils.CostCenterLinked, generic.models.GenericModelWithLines, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, accounting_core.utils.AccountingYearLinked, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('label', models.CharField(max_length=255, verbose_name='Titre')),
                ('quantity', models.DecimalField(default=1, verbose_name='Quantit\xe9', max_digits=20, decimal_places=0)),
                ('value', models.DecimalField(verbose_name='Montant unitaire (HT)', max_digits=20, decimal_places=2)),
                ('tva', models.DecimalField(verbose_name='VAT', max_digits=20, decimal_places=2)),
                ('value_ttc', models.DecimalField(verbose_name='Montant (TTC)', max_digits=20, decimal_places=2)),
                ('invoice', models.ForeignKey(related_name='lines', to='accounting_tools.Invoice', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvoiceLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.Invoice', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvoiceTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('object', models.ForeignKey(related_name='tags', to='accounting_tools.Invoice', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvoiceViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.Invoice', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkedInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('user_pk', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=50, verbose_name='Pr\xe9nom')),
                ('last_name', models.CharField(max_length=50, verbose_name='Nom de famille')),
                ('address', models.TextField(verbose_name='Adresse')),
                ('phone', models.CharField(max_length=20, verbose_name='Num\xe9ro de t\xe9l\xe9phone')),
                ('bank', models.CharField(max_length=128, verbose_name='Nom de la banque')),
                ('iban_ccp', models.CharField(max_length=128, verbose_name='IBAN / CCP')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.deletion.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderInvoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Titre de la facture fournisseur')),
                ('comment', models.TextField(null=True, verbose_name='Commentaire', blank=True)),
                ('reference_number', models.CharField(max_length=255, null=True, verbose_name='Num\xe9ro de R\xe9f\xe9rence', blank=True)),
                ('raw_pay_code', models.TextField(null=True, verbose_name='Raw Swiss Payment Code', blank=True)),
                ('currency', models.CharField(default=b'CHF', max_length=3, verbose_name='Devise', choices=[(b'AED', b'AED'), (b'AFN', b'AFN'), (b'ALL', b'ALL'), (b'AMD', b'AMD'), (b'ANG', b'ANG'), (b'AOA', b'AOA'), (b'ARS', b'ARS'), (b'AUD', b'AUD'), (b'AWG', b'AWG'), (b'AZN', b'AZN'), (b'BAM', b'BAM'), (b'BBD', b'BBD'), (b'BDT', b'BDT'), (b'BGN', b'BGN'), (b'BHD', b'BHD'), (b'BIF', b'BIF'), (b'BMD', b'BMD'), (b'BND', b'BND'), (b'BOB', b'BOB'), (b'BOV', b'BOV'), (b'BRL', b'BRL'), (b'BSD', b'BSD'), (b'BTN', b'BTN'), (b'BWP', b'BWP'), (b'BYN', b'BYN'), (b'BZD', b'BZD'), (b'CAD', b'CAD'), (b'CDF', b'CDF'), (b'CHE', b'CHE'), (b'CHF', b'CHF'), (b'CHW', b'CHW'), (b'CLF', b'CLF'), (b'CLP', b'CLP'), (b'CNY', b'CNY'), (b'COP', b'COP'), (b'COU', b'COU'), (b'CRC', b'CRC'), (b'CUC', b'CUC'), (b'CUP', b'CUP'), (b'CVE', b'CVE'), (b'CZK', b'CZK'), (b'DJF', b'DJF'), (b'DKK', b'DKK'), (b'DOP', b'DOP'), (b'DZD', b'DZD'), (b'EGP', b'EGP'), (b'ERN', b'ERN'), (b'ETB', b'ETB'), (b'EUR', b'EUR'), (b'FJD', b'FJD'), (b'FKP', b'FKP'), (b'GBP', b'GBP'), (b'GEL', b'GEL'), (b'GHS', b'GHS'), (b'GIP', b'GIP'), (b'GMD', b'GMD'), (b'GNF', b'GNF'), (b'GTQ', b'GTQ'), (b'GYD', b'GYD'), (b'HKD', b'HKD'), (b'HNL', b'HNL'), (b'HRK', b'HRK'), (b'HTG', b'HTG'), (b'HUF', b'HUF'), (b'IDR', b'IDR'), (b'ILS', b'ILS'), (b'INR', b'INR'), (b'IQD', b'IQD'), (b'IRR', b'IRR'), (b'ISK', b'ISK'), (b'JMD', b'JMD'), (b'JOD', b'JOD'), (b'JPY', b'JPY'), (b'KES', b'KES'), (b'KGS', b'KGS'), (b'KHR', b'KHR'), (b'KMF', b'KMF'), (b'KPW', b'KPW'), (b'KRW', b'KRW'), (b'KWD', b'KWD'), (b'KYD', b'KYD'), (b'KZT', b'KZT'), (b'LAK', b'LAK'), (b'LBP', b'LBP'), (b'LKR', b'LKR'), (b'LRD', b'LRD'), (b'LSL', b'LSL'), (b'LYD', b'LYD'), (b'MAD', b'MAD'), (b'MDL', b'MDL'), (b'MGA', b'MGA'), (b'MKD', b'MKD'), (b'MMK', b'MMK'), (b'MNT', b'MNT'), (b'MOP', b'MOP'), (b'MRU', b'MRU'), (b'MUR', b'MUR'), (b'MVR', b'MVR'), (b'MWK', b'MWK'), (b'MXN', b'MXN'), (b'MXV', b'MXV'), (b'MYR', b'MYR'), (b'MZN', b'MZN'), (b'NAD', b'NAD'), (b'NGN', b'NGN'), (b'NIO', b'NIO'), (b'NOK', b'NOK'), (b'NPR', b'NPR'), (b'NZD', b'NZD'), (b'OMR', b'OMR'), (b'PAB', b'PAB'), (b'PEN', b'PEN'), (b'PGK', b'PGK'), (b'PHP', b'PHP'), (b'PKR', b'PKR'), (b'PLN', b'PLN'), (b'PYG', b'PYG'), (b'QAR', b'QAR'), (b'RON', b'RON'), (b'RSD', b'RSD'), (b'RUB', b'RUB'), (b'RWF', b'RWF'), (b'SAR', b'SAR'), (b'SBD', b'SBD'), (b'SCR', b'SCR'), (b'SDG', b'SDG'), (b'SEK', b'SEK'), (b'SGD', b'SGD'), (b'SHP', b'SHP'), (b'SLL', b'SLL'), (b'SOS', b'SOS'), (b'SRD', b'SRD'), (b'SSP', b'SSP'), (b'STN', b'STN'), (b'SVC', b'SVC'), (b'SYP', b'SYP'), (b'SZL', b'SZL'), (b'THB', b'THB'), (b'TJS', b'TJS'), (b'TMT', b'TMT'), (b'TND', b'TND'), (b'TOP', b'TOP'), (b'TRY', b'TRY'), (b'TTD', b'TTD'), (b'TWD', b'TWD'), (b'TZS', b'TZS'), (b'UAH', b'UAH'), (b'UGX', b'UGX'), (b'USD', b'USD'), (b'USN', b'USN'), (b'UYI', b'UYI'), (b'UYU', b'UYU'), (b'UYW', b'UYW'), (b'UZS', b'UZS'), (b'VES', b'VES'), (b'VND', b'VND'), (b'VUV', b'VUV'), (b'WST', b'WST'), (b'XAF', b'XAF'), (b'XCD', b'XCD'), (b'XOF', b'XOF'), (b'XPF', b'XPF'), (b'YER', b'YER'), (b'ZAR', b'ZAR'), (b'ZMW', b'ZMW'), (b'ZWL', b'ZWL')])),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'6_canceled', 'Annul\xe9'), (b'3_agep_sig2', 'Attente signature CdD 2'), (b'6_archived', 'Archiv\xe9'), (b'3_agep_sig1', 'Attente signature CdD 1'), (b'2_agep_validable', 'Attente v\xe9rification secr\xe9tariat'), (b'0_correct', 'Corrections n\xe9cessaires'), (b'0_draft', 'Brouillon'), (b'5_in_accounting', 'En comptabilisation'), (b'1_unit_validable', 'Attente accord unit\xe9'), (b'4_accountable', 'A comptabiliser')])),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
                ('provider', models.ForeignKey(verbose_name='Fournisseur', to='accounting_tools.FinancialProvider', on_delete=models.deletion.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericTaggableObject, generic.models.GenericAccountingStateModel, generic.models.GenericStateModel, generic.models.GenericModelWithFiles, generic.models.GenericModelWithLines, accounting_core.utils.AccountingYearLinked, accounting_core.utils.CostCenterLinked, rights.utils.UnitEditableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.LinkedInfoModel, accounting_core.models.AccountingGroupModels, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='ProviderInvoiceFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'uploads/_generic/ProviderInvoice/')),
                ('object', models.ForeignKey(related_name='files', blank=True, to='accounting_tools.ProviderInvoice', null=True, on_delete=models.deletion.SET_NULL)),
                ('uploader', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderInvoiceLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('label', models.CharField(max_length=255, verbose_name='Concerne')),
                ('value', models.DecimalField(verbose_name='Montant (HT)', max_digits=20, decimal_places=2)),
                ('tva', models.DecimalField(verbose_name='VAT', max_digits=20, decimal_places=2)),
                ('value_ttc', models.DecimalField(verbose_name='Montant (TTC)', max_digits=20, decimal_places=2)),
                ('account', models.ForeignKey(verbose_name='Account', to='accounting_core.Account', on_delete=models.deletion.CASCADE)),
                ('providerInvoice', models.ForeignKey(related_name='lines', to='accounting_tools.ProviderInvoice', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderInvoiceLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.ProviderInvoice', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderInvoiceTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('object', models.ForeignKey(related_name='tags', to='accounting_tools.ProviderInvoice', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderInvoiceViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.ProviderInvoice', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subvention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom du projet')),
                ('amount_asked', models.IntegerField(verbose_name='Montant demand\xe9')),
                ('amount_given', models.IntegerField(null=True, verbose_name='Montant attribu\xe9', blank=True)),
                ('mobility_asked', models.IntegerField(null=True, verbose_name='Montant mobilit\xe9 demand\xe9', blank=True)),
                ('mobility_given', models.IntegerField(null=True, verbose_name='Montant mobilit\xe9 attribu\xe9', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('comment_root', models.TextField(null=True, verbose_name='Commentaire AGEPoly', blank=True)),
                ('kind', models.CharField(blank=True, max_length=15, null=True, verbose_name='Type de soutien', choices=[(b'subvention', 'Subvention'), (b'sponsorship', 'Sponsoring')])),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'0_correct', 'A corriger'), (b'0_draft', 'Brouillon'), (b'1_submited', 'Demande soumise'), (b'2_treated', 'Demande trait\xe9e')])),
                ('unit_blank_name', models.CharField(max_length=255, null=True, verbose_name="Nom de l'entit\xe9 externe", blank=True)),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('linked_budget', models.ForeignKey(verbose_name='Budget annuel li\xe9', blank=True, to='accounting_main.Budget', null=True, on_delete=models.deletion.SET_NULL)),
                ('unit', models.ForeignKey(blank=True, to='units.Unit', null=True, on_delete=models.deletion.SET_NULL)),
                ('unit_blank_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericModelWithFiles, generic.models.GenericModelWithLines, accounting_core.utils.AccountingYearLinked, generic.models.GenericStateModel, generic.models.GenericGroupsModel, rights.utils.UnitExternalEditableModel, generic.models.GenericExternalUnitAllowed, generic.models.GenericContactableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='SubventionFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'uploads/_generic/Subvention/')),
                ('object', models.ForeignKey(related_name='files', blank=True, to='accounting_tools.Subvention', null=True, on_delete=models.deletion.SET_NULL)),
                ('uploader', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubventionLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('name', models.CharField(max_length=255, verbose_name="Nom de l'\xe9v\xe8nement")),
                ('start_date', models.DateField(verbose_name="D\xe9but de l'\xe9v\xe8nement")),
                ('end_date', models.DateField(verbose_name="Fin de l'\xe9v\xe8nement")),
                ('place', models.CharField(max_length=100, verbose_name="Lieu de l'\xe9v\xe8nement")),
                ('nb_spec', models.PositiveIntegerField(verbose_name='Nombre de personnes attendues')),
                ('subvention', models.ForeignKey(related_name='events', verbose_name='Subvention/sponsoring', to='accounting_tools.Subvention', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubventionLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.Subvention', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubventionViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.Subvention', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Raison du retrait')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('amount', models.DecimalField(verbose_name='Montant', max_digits=20, decimal_places=2)),
                ('desired_date', models.DateField(verbose_name='Date souhait\xe9e')),
                ('withdrawn_date', models.DateField(null=True, verbose_name='Date r\xe9elle de retrait', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'3_used', 'R\xe9cup\xe9r\xe9 / A justifier'), (b'1_agep_validable', 'Attente accord AGEPoly'), (b'0_draft', 'Brouillon'), (b'4_canceled', 'Annul\xe9'), (b'2_withdrawn', 'Pr\xeat \xe0 \xeatre r\xe9cup\xe9r\xe9'), (b'4_archived', 'Archiv\xe9')])),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
                ('user', models.ForeignKey(verbose_name='Responsable', to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, generic.models.GenericTaggableObject, generic.models.GenericModelWithFiles, accounting_core.utils.AccountingYearLinked, accounting_core.utils.CostCenterLinked, rights.utils.UnitEditableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.LinkedInfoModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='WithdrawalFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'uploads/_generic/Withdrawal/')),
                ('object', models.ForeignKey(related_name='files', blank=True, to='accounting_tools.Withdrawal', null=True, on_delete=models.deletion.SET_NULL)),
                ('uploader', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithdrawalLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_tools.Withdrawal', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithdrawalTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('object', models.ForeignKey(related_name='tags', to='accounting_tools.Withdrawal', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithdrawalViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_tools.Withdrawal', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
