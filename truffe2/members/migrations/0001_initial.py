# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import generic.models
import generic.search
import rights.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('generates_accred', models.BooleanField(default=True, verbose_name='G\xe9n\xe8re des accreds')),
                ('ldap_visible', models.BooleanField(default=False, verbose_name="Rend les accreds visibles dans l'annuaire")),
                ('handle_fees', models.BooleanField(default=False, verbose_name='Gestion des cotisations')),
                ('api_secret_key', models.CharField(max_length=128, null=True, verbose_name="Cl\xe9 secr\xe8te pour l'API", blank=True)),
                ('status', models.CharField(default=b'0_preparing', max_length=255, choices=[(b'1_active', 'Actif'), (b'2_archived', 'Archiv\xe9'), (b'0_preparing', 'En pr\xe9paration')])),
                ('generated_accred_type', models.ForeignKey(verbose_name='Accr\xe9ditation g\xe9n\xe9r\xe9e pour les membres', blank=True, to='units.Role', null=True, on_delete=models.deletion.SET_NULL)),
                ('unit', models.ForeignKey(verbose_name='Unit\xe9', to='units.Unit', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, generic.models.GenericGroupsModel, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='MemberSetLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='members.MemberSet', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberSetViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='members.MemberSet', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout au groupe")),
                ('end_date', models.DateTimeField(null=True, verbose_name='Date de retrait du groupe', blank=True)),
                ('payed_fees', models.BooleanField(default=False, verbose_name='A pay\xe9 sa cotisation')),
                ('group', models.ForeignKey(verbose_name='Groupe de membres', to='members.MemberSet', on_delete=models.deletion.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='memberset',
            unique_together=set([('name', 'unit')]),
        ),
    ]
