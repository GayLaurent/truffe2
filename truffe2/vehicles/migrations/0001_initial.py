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
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('reason', models.TextField(verbose_name='Motif')),
                ('remark', models.TextField(null=True, verbose_name='Remarques', blank=True)),
                ('remark_agepoly', models.TextField(null=True, verbose_name='Remarques AGEPoly', blank=True)),
                ('start_date', models.DateTimeField(verbose_name='D\xe9but de la r\xe9servation')),
                ('end_date', models.DateTimeField(verbose_name='Fin de la r\xe9servation')),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'4_deny', 'Refus\xe9'), (b'4_canceled', 'Annul\xe9'), (b'0_draft', 'Brouillon'), (b'3_archive', 'Archiv\xe9'), (b'1_asking', 'Validation en cours'), (b'2_online', 'Valid\xe9')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericGroupsModerableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.GenericStateRootValidable, generic.models.GenericStateModel, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='BookingLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='vehicles.Booking', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='vehicles.Booking', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('number', models.CharField(max_length=255, verbose_name='Num\xe9ro')),
                ('description', models.TextField(verbose_name='Description')),
                ('exclusif', models.BooleanField(default=True, help_text='Ne peut pas \xeatre utilis\xe9 plusieurs fois en m\xeame temps ?', verbose_name='Usage exclusif')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='CardLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='vehicles.Card', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='vehicles.Card', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('url_location', models.URLField(null=True, verbose_name='URL carte lieu', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='LocationLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='vehicles.Location', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='vehicles.Location', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='ProviderLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='vehicles.Provider', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='vehicles.Provider', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('provider', models.ForeignKey(verbose_name='Fournisseur', to='vehicles.Provider', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='VehicleTypeLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='vehicles.VehicleType', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VehicleTypeViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='vehicles.VehicleType', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='provider',
            field=models.ForeignKey(verbose_name='Fournisseur', to='vehicles.Provider', on_delete=models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='card',
            field=models.ForeignKey(verbose_name='Carte', blank=True, to='vehicles.Card', null=True, on_delete=models.deletion.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(verbose_name='Lieu', blank=True, to='vehicles.Location', null=True, on_delete=models.deletion.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='provider',
            field=models.ForeignKey(verbose_name='Fournisseur', to='vehicles.Provider', on_delete=models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='responsible',
            field=models.ForeignKey(verbose_name='Responsable', to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='unit',
            field=models.ForeignKey(to='units.Unit', on_delete=models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicletype',
            field=models.ForeignKey(verbose_name='Type de v\xe9hicule', to='vehicles.VehicleType', on_delete=models.deletion.CASCADE),
            preserve_default=True,
        ),
    ]
