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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '__first__'),
        ('accounting_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingError',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('linked_line_cache', models.CharField(max_length=4096)),
                ('initial_remark', models.TextField(help_text='D\xe9crit le probl\xe8me', verbose_name='Remarque initiale')),
                ('status', models.CharField(default=b'0_drafting', max_length=255, choices=[(b'2_fixed', 'Correction effectu\xe9e'), (b'1_fixing', 'En attente de correction'), (b'0_drafting', '\xc9tablisement du probl\xe8me')])),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, accounting_core.utils.AccountingYearLinked, accounting_core.utils.CostCenterLinked, generic.models.GenericGroupsModel, accounting_core.models.AccountingGroupModels, generic.models.GenericContactableModel, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='AccountingErrorLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_main.AccountingError', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountingErrorMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
                ('error', models.ForeignKey(to='accounting_main.AccountingError', on_delete=models.deletion.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountingErrorViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_main.AccountingError', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountingLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('tva', models.DecimalField(verbose_name='VAT', max_digits=20, decimal_places=2)),
                ('text', models.CharField(max_length=2048)),
                ('output', models.DecimalField(verbose_name='D\xe9bit', max_digits=20, decimal_places=2)),
                ('input', models.DecimalField(verbose_name='Cr\xe9dit', max_digits=20, decimal_places=2)),
                ('current_sum', models.DecimalField(verbose_name='Situation', max_digits=20, decimal_places=2)),
                ('document_id', models.PositiveIntegerField(null=True, verbose_name='Num\xe9ro de pi\xe8ce comptable', blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default=b'0_imported', max_length=255, choices=[(b'0_imported', 'En attente'), (b'2_error', 'Erreur'), (b'1_validated', 'Valid\xe9')])),
                ('account', models.ForeignKey(verbose_name='Compte de CG', to='accounting_core.Account', on_delete=models.deletion.CASCADE)),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, accounting_core.utils.AccountingYearLinked, accounting_core.utils.CostCenterLinked, generic.models.GenericGroupsModel, accounting_core.models.AccountingGroupModels, generic.models.GenericContactableModel, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='AccountingLineLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_main.AccountingLine', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountingLineViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_main.AccountingLine', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Titre du budget')),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'0_correct', 'A corriger'), (b'0_draft', 'Brouillon'), (b'1_private', 'Budget priv\xe9'), (b'1_submited', 'Budget soumis'), (b'2_treated', 'Budget valid\xe9')])),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.CASCADE)),
                ('costcenter', models.ForeignKey(verbose_name='Centre de co\xfbt', to='accounting_core.CostCenter', on_delete=models.deletion.CASCADE)),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, accounting_core.utils.AccountingYearLinked, accounting_core.utils.CostCenterLinked, rights.utils.UnitEditableModel, generic.models.GenericContactableModel, generic.models.GenericTaggableObject, accounting_core.models.AccountingGroupModels, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='BudgetLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(verbose_name='Montant', max_digits=20, decimal_places=2)),
                ('description', models.CharField(max_length=250)),
                ('account', models.ForeignKey(verbose_name='Account', to='accounting_core.Account', on_delete=models.deletion.CASCADE)),
                ('budget', models.ForeignKey(verbose_name='Budget', to='accounting_main.Budget', on_delete=models.deletion.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_main.Budget', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('object', models.ForeignKey(related_name='tags', to='accounting_main.Budget', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_main.Budget', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='accountingerror',
            name='linked_line',
            field=models.ForeignKey(verbose_name='Ligne li\xe9e', blank=True, to='accounting_main.AccountingLine', null=True, on_delete=models.deletion.SET_NULL),
            preserve_default=True,
        ),
    ]
