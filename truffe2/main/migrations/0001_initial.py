# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import generic.models
from django.conf import settings
import generic.search
import rights.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('file', models.FileField(upload_to=b'uploads/files/')),
                ('access', models.CharField(default=b'agep', max_length=64, verbose_name='Acc\xe8s', choices=[(b'agep', "Selement les membres d'une unit\xe9"), (b'all', 'Tous les utilisateurs')])),
                ('group', models.CharField(default=b'misc', max_length=64, verbose_name='Groupe', choices=[(b'accounting', 'Finances'), (b'cs', 'Informatique'), (b'misc', 'Divers')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='FileLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='main.File', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='main.File', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePageNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(default=b'0_draft', max_length=255, choices=[(b'2_archive', 'Archiv\xe9'), (b'0_draft', 'Brouillon'), (b'1_online', 'En ligne')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, generic.models.GenericStateModel, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='HomePageNewsLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='main.HomePageNews', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePageNewsViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='main.HomePageNews', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('url', models.URLField()),
                ('leftmenu', models.CharField(choices=[(b'/main/top', 'Principal / En haut'), (b'/main/bottom', 'Principal / En bas'), (b'/admin/', 'Admin'), (b'/gens/', 'Gens'), (b'/communication/', 'Communication'), (b'/logistics/', 'Logistique'), (b'/logistics/vehicles', 'Logistique / V\xe9hicules'), (b'/logistics/rooms', 'Logistique / Salles'), (b'/logistics/supply', 'Logistique / Mat\xe9riel'), (b'/units/', 'Unit\xe9s et Accreds'), (b'/accounting/', 'Finances'), (b'/accounting/accounting', 'Finances / Compta'), (b'/accounting/tools', 'Finances / Outils'), (b'/accounting/proofs', 'Finances / Justifications'), (b'/accounting/gestion', 'Finances / Gestion'), (b'/cs/', 'Informatique'), (b'/misc/', 'Divers')], max_length=128, blank=True, help_text="Laisser blanc pour faire un lien normal. R\xe9serv\xe9 au comit\xe9 de l'AGEPoly. Attention, cache de 15 minutes !", null=True, verbose_name='Position dans le menu de gauche')),
                ('icon', models.CharField(default=b'fa-external-link-square', max_length=128, verbose_name='Icone FontAwesome')),
                ('unit', models.ForeignKey(to='units.Unit', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='LinkLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='main.Link', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='main.Link', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SignableDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('file', models.FileField(upload_to=b'uploads/signable_document/')),
                ('active', models.BooleanField(default=False, verbose_name='Actif')),
                ('sha', models.CharField(max_length=255)),
                ('roles', models.ManyToManyField(to='units.Role')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='SignableDocumentLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='main.SignableDocument', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SignableDocumentViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='main.SignableDocument', on_delete=models.deletion.CASCADE)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('useragent', models.CharField(max_length=255)),
                ('document_sha', models.CharField(max_length=255)),
                ('document', models.ForeignKey(to='main.SignableDocument', on_delete=models.deletion.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
