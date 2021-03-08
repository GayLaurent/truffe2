# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounting_core.utils
import generic.search
import rights.utils
import generic.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom du compte')),
                ('account_number', models.CharField(max_length=10, verbose_name='Num\xe9ro du compte')),
                ('visibility', models.CharField(max_length=50, verbose_name='Visibilit\xe9 dans les documents comptables', choices=[(b'all', 'Visible \xe0 tous'), (b'cdd', 'Visible au Comit\xe9 de Direction uniquement'), (b'root', 'Visible aux personnes qui g\xe8re la comptabilit\xe9 g\xe9n\xe9rale'), (b'none', 'Visible \xe0 personne')])),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, accounting_core.utils.AccountingYearLinked, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom de la cat\xe9gorie')),
                ('order', models.SmallIntegerField(default=0, help_text="Le plus petit d'abord", verbose_name='Ordre dans le plan comptable')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, accounting_core.utils.AccountingYearLinked, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='AccountCategoryLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_core.AccountCategory', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountCategoryViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_core.AccountCategory', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountingYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Date de d\xe9but', blank=True)),
                ('end_date', models.DateTimeField(null=True, verbose_name='Date de fin', blank=True)),
                ('subvention_deadline', models.DateTimeField(null=True, verbose_name='D\xe9lai pour les subventions', blank=True)),
                ('last_accounting_import', models.DateTimeField(null=True, verbose_name='Dernier import de la compta', blank=True)),
                ('status', models.CharField(default=b'0_preparing', max_length=255, choices=[(b'1_active', 'Ann\xe9e active'), (b'3_archived', 'Ann\xe9e archiv\xe9e'), (b'0_preparing', 'En pr\xe9paration'), (b'2_closing', 'En cl\xf4ture')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='AccountingYearLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_core.AccountingYear', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountingYearViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_core.AccountingYear', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_core.Account', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_core.Account', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom du centre de co\xfbt')),
                ('account_number', models.CharField(max_length=10, verbose_name='Num\xe9ro associ\xe9 au centre de co\xfbt')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('accounting_year', models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.PROTECT)),
                ('unit', models.ForeignKey(verbose_name='Appartient \xe0', to='units.Unit', on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, accounting_core.utils.AccountingYearLinked, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='CostCenterLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_core.CostCenter', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CostCenterViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_core.CostCenter', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TVA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom de la TVA')),
                ('value', models.DecimalField(verbose_name='Valeur (%)', max_digits=20, decimal_places=2)),
                ('agepoly_only', models.BooleanField(default=False, verbose_name="Limiter l'usage au comit\xe9 de l'AGEPoly")),
                ('code', models.CharField(max_length=255, verbose_name='Code de TVA')),
                ('account', models.ForeignKey(verbose_name='Compte de TVA', to='accounting_core.Account', on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='TVALogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='accounting_core.TVA', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TVAViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='accounting_core.TVA', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='costcenter',
            unique_together=set([('name', 'accounting_year'), ('account_number', 'accounting_year')]),
        ),
        migrations.AddField(
            model_name='accountcategory',
            name='accounting_year',
            field=models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accountcategory',
            name='parent_hierarchique',
            field=models.ForeignKey(blank=True, to='accounting_core.AccountCategory', help_text='Cat\xe9gorie parente pour la hi\xe9rarchie', null=True, on_delete=models.deletion.SET_NULL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='accountcategory',
            unique_together=set([('name', 'accounting_year')]),
        ),
        migrations.AddField(
            model_name='account',
            name='accounting_year',
            field=models.ForeignKey(verbose_name='Ann\xe9e comptable', to='accounting_core.AccountingYear', on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='category',
            field=models.ForeignKey(verbose_name='Cat\xe9gorie', to='accounting_core.AccountCategory', on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('name', 'accounting_year'), ('account_number', 'accounting_year')]),
        ),
    ]
