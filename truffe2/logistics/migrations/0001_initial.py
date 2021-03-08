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
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True, help_text='Pour d\xe9sactiver temporairement la posibilit\xe9 de r\xe9server.', verbose_name='Actif')),
                ('conditions', models.TextField(help_text='Si tu veux pr\xe9ciser les conditions de r\xe9servation pour la salle. Tu peux par exemple mettre un lien vers un contrat.', verbose_name='Conditions de r\xe9servation', blank=True)),
                ('allow_externals', models.BooleanField(default=False, help_text="Permet aux externes (pas dans l'AGEPoly) de r\xe9server la salle.", verbose_name='Autoriser les externes')),
                ('conditions_externals', models.TextField(help_text="Si tu veux pr\xe9ciser des informations sur la r\xe9servation de la salle pour les externes. Remplace le champ 'Conditions' pour les externe si rempli.", verbose_name='Conditions de r\xe9servation pour les externes', blank=True)),
                ('allow_calendar', models.BooleanField(default=True, help_text="Permet \xe0 tout le monde d'afficher le calendrier des r\xe9servations de la salle", verbose_name='Autoriser tout le monde \xe0 voir le calendrier')),
                ('allow_external_calendar', models.BooleanField(default=True, help_text="Permet aux externes d'afficher le calendrier des r\xe9servations de la salle. Le calendrier doit \xeatre visible.", verbose_name='Autoriser les externes \xe0 voir le calendrier')),
                ('max_days', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la longeur de la r\xe9servation dure plus longtemps que le nombre de jours d\xe9fini.', verbose_name='Nombre maximum de jours de r\xe9servation')),
                ('max_days_externals', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la longeur de la r\xe9servation dure plus longtemps que le nombre de jours d\xe9fini, pour les unit\xe9s externes.', verbose_name='Nombre maximum de jours de r\xe9servation (externes)')),
                ('minimum_days_before', models.PositiveIntegerField(default=0, help_text="Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation n'est pas au moins dans X jours.", verbose_name='Nombre de jours minimum avant r\xe9servation')),
                ('minimum_days_before_externals', models.PositiveIntegerField(default=0, help_text="Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation n'est pas au plus dans X jours, pour les externes.", verbose_name='Nombre de jours minimum avant r\xe9servation (externes)')),
                ('maximum_days_before', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation est dans plus de X jours.', verbose_name='Nombre de jours maximum avant r\xe9servation')),
                ('maximum_days_before_externals', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation est dans plus de X jours, pour les externes.', verbose_name='Nombre de jours maximum avant r\xe9servation (externes)')),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericGroupsModel, rights.utils.UnitEditableModel, generic.models.GenericDelayValidableInfo, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='RoomLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='logistics.Room', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('start_date', models.DateTimeField(verbose_name='Date de d\xe9but')),
                ('end_date', models.DateTimeField(verbose_name='Date de fin')),
                ('reason', models.TextField(help_text='Explique bri\xe8vement ce que tu vas faire', verbose_name='Raison')),
                ('remarks', models.TextField(null=True, verbose_name='Remarques', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'4_deny', 'Refus\xe9'), (b'4_canceled', 'Annul\xe9'), (b'0_draft', 'Brouillon'), (b'3_archive', 'Archiv\xe9'), (b'1_asking', 'Validation en cours'), (b'2_online', 'Valid\xe9')])),
                ('unit_blank_name', models.CharField(max_length=255, null=True, verbose_name="Nom de l'entit\xe9 externe", blank=True)),
                ('room', models.ForeignKey(verbose_name='Salle', to='logistics.Room', on_delete=models.deletion.PROTECT)),
                ('unit', models.ForeignKey(blank=True, to='units.Unit', null=True, on_delete=models.deletion.SET_NULL)),
                ('unit_blank_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericDelayValidable, generic.models.GenericGroupsValidableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.GenericStateUnitValidable, generic.models.GenericStateModel, generic.models.GenericExternalUnitAllowed, rights.utils.UnitExternalEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='RoomReservationLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='logistics.RoomReservation', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomReservationViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='logistics.RoomReservation', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='logistics.Room', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField(default=1, help_text="Le nombre de fois que tu as l'objet \xe0 disposition", verbose_name='Quantit\xe9')),
                ('price', models.PositiveIntegerField(default=0, help_text='Le prix en CHF de remplacement du mat\xe9riel, en cas de casse ou de perte', verbose_name='Prix')),
                ('active', models.BooleanField(default=True, help_text='Pour d\xe9sactiver temporairement la posibilit\xe9 de r\xe9server.', verbose_name='Actif')),
                ('conditions', models.TextField(help_text='Si tu veux pr\xe9ciser les conditions de r\xe9servations pour le mat\xe9riel. Tu peux par exemple mettre un lien vers un contrat.', verbose_name='Conditions de r\xe9servation', blank=True)),
                ('allow_externals', models.BooleanField(default=False, help_text="Permet aux externes (pas dans l'AGEPoly) de r\xe9server le mat\xe9riel.", verbose_name='Autoriser les externes')),
                ('conditions_externals', models.TextField(help_text="Si tu veux pr\xe9ciser des informations sur la r\xe9servation du mat\xe9riel pour les externes. Remplace le champ 'Conditions' pour les externe si rempli.", verbose_name='Conditions de r\xe9servation pour les externes', blank=True)),
                ('allow_calendar', models.BooleanField(default=True, help_text="Permet \xe0 tout le monde d'afficher le calendrier des r\xe9servations du mat\xe9riel", verbose_name='Autoriser tout le monde \xe0 voir le calendrier')),
                ('allow_external_calendar', models.BooleanField(default=True, help_text="Permet aux externes d'afficher le calendrier des r\xe9servations du mat\xe9riel. Le calendrier doit \xeatre visible.", verbose_name='Autoriser les externes \xe0 voir le calendrier')),
                ('max_days', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la longeur de la r\xe9servation dure plus longtemps que le nombre de jours d\xe9fini.', verbose_name='Nombre maximum de jours de r\xe9servation')),
                ('max_days_externals', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la longeur de la r\xe9servation dure plus longtemps que le nombre de jours d\xe9fini, pour les unit\xe9s externes.', verbose_name='Nombre maximum de jours de r\xe9servation (externes)')),
                ('minimum_days_before', models.PositiveIntegerField(default=0, help_text="Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation n'est pas au moins dans X jours.", verbose_name='Nombre de jours minimum avant r\xe9servation')),
                ('minimum_days_before_externals', models.PositiveIntegerField(default=0, help_text="Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation n'est pas au plus dans X jours, pour les externes.", verbose_name='Nombre de jours minimum avant r\xe9servation (externes)')),
                ('maximum_days_before', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation est dans plus de X jours.', verbose_name='Nombre de jours maximum avant r\xe9servation')),
                ('maximum_days_before_externals', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation est dans plus de X jours, pour les externes.', verbose_name='Nombre de jours maximum avant r\xe9servation (externes)')),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericGroupsModel, rights.utils.UnitEditableModel, generic.models.GenericDelayValidableInfo, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='SupplyLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='logistics.Supply', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplyReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(help_text='Par exemple le nom de ton \xe9v\xe9nement', max_length=255, verbose_name='Nom de la r\xe9servation')),
                ('start_date', models.DateTimeField(help_text='Date et heure souhait\xe9es pour la prise du mat\xe9riel', verbose_name='Date de d\xe9but')),
                ('end_date', models.DateTimeField(help_text='Date et heure souhait\xe9es pour le retour du mat\xe9riel', verbose_name='Date de fin')),
                ('contact_phone', models.CharField(max_length=25, verbose_name='T\xe9l\xe9phone de contact')),
                ('reason', models.TextField(help_text='Explique bri\xe8vement ce que tu vas faire', verbose_name='Raison')),
                ('remarks', models.TextField(null=True, verbose_name='Remarques', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'4_deny', 'Refus\xe9'), (b'4_canceled', 'Annul\xe9'), (b'0_draft', 'Brouillon'), (b'3_archive', 'Archiv\xe9'), (b'1_asking', 'Validation en cours'), (b'2_online', 'Valid\xe9')])),
                ('unit_blank_name', models.CharField(max_length=255, null=True, verbose_name="Nom de l'entit\xe9 externe", blank=True)),
                ('unit', models.ForeignKey(blank=True, to='units.Unit', null=True, on_delete=models.deletion.SET_NULL)),
                ('unit_blank_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericModelWithLines, generic.models.GenericDelayValidable, generic.models.GenericGroupsValidableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.GenericStateUnitValidable, generic.models.GenericStateModel, generic.models.GenericExternalUnitAllowed, rights.utils.UnitExternalEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='SupplyReservationLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantit\xe9')),
                ('supply', models.ForeignKey(related_name='reservations', to='logistics.Supply', on_delete=models.deletion.PROTECT)),
                ('supply_reservation', models.ForeignKey(related_name='lines', to='logistics.SupplyReservation', on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplyReservationLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='logistics.SupplyReservation', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplyReservationViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='logistics.SupplyReservation', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplyViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='logistics.Supply', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
