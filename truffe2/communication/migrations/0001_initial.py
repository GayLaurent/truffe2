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
            name='AgepSlide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('picture', models.ImageField(help_text="Pour des raisons de qualit\xe9, il est fortement recommand\xe9 d'envoyer une image en HD (1920x1080)", upload_to=b'uploads/slides/', verbose_name='Image')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Date de d\xe9but', blank=True)),
                ('end_date', models.DateTimeField(null=True, verbose_name='Date de fin', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'4_deny', 'Refus\xe9'), (b'4_canceled', 'Annul\xe9'), (b'0_draft', 'Brouillon'), (b'3_archive', 'Archiv\xe9'), (b'1_asking', 'Mod\xe9ration en cours'), (b'2_online', 'En ligne')])),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericGroupsModerableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.GenericStateRootModerable, generic.models.GenericStateModel, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='AgepSlideLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='communication.AgepSlide', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AgepSlideViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='communication.AgepSlide', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True, help_text='Pour d\xe9sactiver temporairement la posibilit\xe9 de r\xe9server.', verbose_name='Actif')),
                ('conditions', models.TextField(help_text="Si tu veux pr\xe9ciser les conditions de r\xe9servations pour l'affichage. Tu peux par exemple mettre un lien vers un contrat.", verbose_name='Conditions de r\xe9servation', blank=True)),
                ('allow_externals', models.BooleanField(default=False, help_text="Permet aux externes (pas dans l'AGEPoly) de r\xe9server l'affichage.", verbose_name='Autoriser les externes')),
                ('conditions_externals', models.TextField(help_text="Si tu veux pr\xe9ciser des informations sur la r\xe9servation de l'affichage pour les externes. Remplace le champ 'Conditions' pour les externe si rempli.", verbose_name='Conditions de r\xe9servation pour les externes', blank=True)),
                ('allow_calendar', models.BooleanField(default=True, help_text="Permet \xe0 tout le monde d'afficher le calendrier des r\xe9servations de l'affichage", verbose_name='Autoriser tout le monde \xe0 voir le calendrier')),
                ('allow_external_calendar', models.BooleanField(default=True, help_text="Permet aux externes d'afficher le calendrier des r\xe9servations de l'affichage. Le calendrier doit \xeatre visible.", verbose_name='Autoriser les externes \xe0 voir le calendrier')),
                ('max_days', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la longeur de la r\xe9servation dure plus longtemps que le nombre de jours d\xe9fini.', verbose_name='Nombre maximum de jours de r\xe9servation')),
                ('max_days_externals', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la longeur de la r\xe9servation dure plus longtemps que le nombre de jours d\xe9fini, pour les unit\xe9s externes.', verbose_name='Nombre maximum de jours de r\xe9servation (externes)')),
                ('minimum_days_before', models.PositiveIntegerField(default=0, help_text="Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation n'est pas au moins dans X jours.", verbose_name='Nombre de jours minimum avant r\xe9servation')),
                ('minimum_days_before_externals', models.PositiveIntegerField(default=0, help_text="Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation n'est pas au plus dans X jours, pour les externes.", verbose_name='Nombre de jours minimum avant r\xe9servation (externes)')),
                ('maximum_days_before', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation est dans plus de X jours.', verbose_name='Nombre de jours maximum avant r\xe9servation')),
                ('maximum_days_before_externals', models.PositiveIntegerField(default=0, help_text='Si sup\xe9rieur \xe0 z\xe9ro, emp\xeache de demander une r\xe9servation si la r\xe9servation est dans plus de X jours, pour les externes.', verbose_name='Nombre de jours maximum avant r\xe9servation (externes)')),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericGroupsModel, rights.utils.UnitEditableModel, generic.models.GenericDelayValidableInfo, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='DisplayLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='communication.Display', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisplayReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('start_date', models.DateTimeField(verbose_name='Date de d\xe9but')),
                ('end_date', models.DateTimeField(verbose_name='Date de fin')),
                ('reason', models.TextField(help_text='Explique pourquoi tu as besoin (manifestation par ex.)', verbose_name='Raison')),
                ('remarks', models.TextField(null=True, verbose_name='Remarques', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'4_deny', 'Refus\xe9'), (b'4_canceled', 'Annul\xe9'), (b'0_draft', 'Brouillon'), (b'3_archive', 'Archiv\xe9'), (b'1_asking', 'Validation en cours'), (b'2_online', 'Valid\xe9')])),
                ('unit_blank_name', models.CharField(max_length=255, null=True, verbose_name="Nom de l'entit\xe9 externe", blank=True)),
                ('display', models.ForeignKey(verbose_name='Affichage', to='communication.Display', on_delete=models.deletion.CASCADE)),
                ('unit', models.ForeignKey(blank=True, to='units.Unit', null=True, on_delete=models.deletion.SET_NULL)),
                ('unit_blank_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericDelayValidable, generic.models.GenericGroupsValidableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.GenericStateUnitValidable, generic.models.GenericStateModel, generic.models.GenericExternalUnitAllowed, rights.utils.UnitExternalEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='DisplayReservationLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='communication.DisplayReservation', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisplayReservationViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='communication.DisplayReservation', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisplayViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='communication.Display', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('visibility_level', models.CharField(default=b'default', help_text="Permet de rendre l'objet plus visible que les droits de base", max_length=32, verbose_name='Visibilit\xe9', choices=[(b'default', "De base (En fonction de l'objet et des droits)"), (b'unit', 'Unit\xe9 li\xe9e'), (b'unit_agep', "Unit\xe9 li\xe9e et Comit\xe9 de l'AGEPoly"), (b'all_agep', 'Toutes les personnes accr\xe9dit\xe9s dans une unit\xe9'), (b'all', 'Tout le monde')])),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericModelWithFiles, rights.utils.AutoVisibilityLevel, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='LogoFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'uploads/_generic/Logo/')),
                ('object', models.ForeignKey(related_name='files', blank=True, to='communication.Logo', null=True, on_delete=models.deletion.SET_NULL)),
                ('uploader', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LogoLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='communication.Logo', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LogoViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='communication.Logo', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebsiteNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Titre anglais', blank=True)),
                ('content', models.TextField(verbose_name='Contenu')),
                ('content_en', models.TextField(null=True, verbose_name='Contenu anglais', blank=True)),
                ('url', models.URLField(max_length=255)),
                ('start_date', models.DateTimeField(null=True, verbose_name='Date d\xe9but', blank=True)),
                ('end_date', models.DateTimeField(null=True, verbose_name='Date fin', blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'4_deny', 'Refus\xe9'), (b'4_canceled', 'Annul\xe9'), (b'0_draft', 'Brouillon'), (b'3_archive', 'Archiv\xe9'), (b'1_asking', 'Mod\xe9ration en cours'), (b'2_online', 'En ligne')])),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericGroupsModerableModel, generic.models.GenericGroupsModel, generic.models.GenericContactableModel, generic.models.GenericStateRootModerable, generic.models.GenericStateModel, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='WebsiteNewsLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='communication.WebsiteNews', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebsiteNewsViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='communication.WebsiteNews', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
