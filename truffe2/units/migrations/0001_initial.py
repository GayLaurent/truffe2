# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
from django.conf import settings
import generic.search
import rights.utils


def initial_values(apps, schema_editor):
    Unit = apps.get_model('units', 'Unit')
    db_alias = schema_editor.connection.alias
    try:
        Unit.objects.using(db_alias).get(pk=settings.ROOT_UNIT_PK)
    except Unit.DoesNotExist:
        Unit.objects.using(db_alias).bulk_create([
            Unit(pk=settings.ROOT_UNIT_PK, name=u"Comité de Direction de l'AGEPoly", 
                 id_epfl=147, description=u"Le comité de l'AGEPoly", url='https://agepoly.epfl.ch/'),
            ])


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessDelegation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('access', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=97, null=True, choices=[(b'PRESIDENCE', 'Pr\xe9sidence'), (b'TRESORERIE', 'Tr\xe9sorerie'), (b'COMMUNICATION', 'Communication'), (b'INFORMATIQUE', 'Informatique'), (b'ACCREDITATION', 'Accr\xe9ditations'), (b'LOGISTIQUE', 'Logistique'), (b'SECRETARIAT', 'Secr\xe9tariat'), (b'COMMISSIONS', 'Commissions')])),
                ('valid_for_sub_units', models.BooleanField(default=False, help_text="Si s\xe9lectionn\xe9, les acc\xe8s suppl\xe9mentaires dans l'unit\xe9 courante seront aussi valides dans les sous-unit\xe9s", verbose_name='Valide pour les sous-unit\xe9s')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.UnitEditableModel),
        ),
        migrations.CreateModel(
            name='AccessDelegationLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='units.AccessDelegation', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccessDelegationViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='units.AccessDelegation', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Accreditation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('renewal_date', models.DateTimeField(auto_now_add=True)),
                ('display_name', models.CharField(help_text='Pr\xe9cision optionnelle \xe0 afficher dans Truffe. Peut \xeatre utilis\xe9 pour pr\xe9ciser la fonction, par exemple: "Responsable R\xe9seau" pour une accr\xe9ditation de Responsable Informatique.', max_length=255, null=True, verbose_name='Titre', blank=True)),
                ('no_epfl_sync', models.BooleanField(default=False, help_text='A cocher pour ne pas synchroniser cette accr\xe9ditation au niveau EPFL', verbose_name='D\xe9sactiver syncronisation EPFL')),
                ('hidden_in_epfl', models.BooleanField(default=False, help_text="A cocher pour ne pas rendre public l'accr\xe9ditation au niveau EPFL", verbose_name='Cacher au niveau EPFL')),
                ('hidden_in_truffe', models.BooleanField(default=False, help_text="A cocher pour ne pas rendre public l'accr\xe9ditation au niveau truffe (sauf aux accr\xe9diteurs sur la page d'accr\xe9ditation)", verbose_name='Cacher dans Truffe')),
                ('need_validation', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model, rights.utils.UnitEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='AccreditationLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('what', models.TextField(null=True, blank=True)),
                ('type', models.CharField(max_length=32, choices=[(b'created', 'Cr\xe9\xe9e'), (b'edited', 'Modifi\xe9e'), (b'deleted', 'Supprim\xe9e'), (b'autodeleted', 'Supprim\xe9e automatiquement'), (b'renewed', 'Renouvel\xe9e'), (b'validated', 'Valid\xe9e'), (b'autocreated', 'Cr\xe9\xe9e automatiquement')])),
                ('accreditation', models.ForeignKey(to='units.Accreditation', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('id_epfl', models.CharField(help_text="Mettre ici l'ID accred du r\xf4le pour la synchronisation EPFL", max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('order', models.IntegerField(help_text="Il n'est pas possible d'accr\xe9diter la m\xeame personne dans la m\xeame unit\xe9 plusieurs fois. Le r\xf4le avec le plus PETIT ordre sera pris en compte", null=True, blank=True)),
                ('need_validation', models.BooleanField(default=False, help_text="A cocher pour indiquer que le comit\xe9 de l'AGEPoly doit valider l'attribution du r\xf4le", verbose_name='N\xe9cessite validation')),
                ('access', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=97, null=True, choices=[(b'PRESIDENCE', 'Pr\xe9sidence'), (b'TRESORERIE', 'Tr\xe9sorerie'), (b'COMMUNICATION', 'Communication'), (b'INFORMATIQUE', 'Informatique'), (b'ACCREDITATION', 'Accr\xe9ditations'), (b'LOGISTIQUE', 'Logistique'), (b'SECRETARIAT', 'Secr\xe9tariat'), (b'COMMISSIONS', 'Commissions')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='RoleLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='units.Role', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoleViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='units.Role', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('id_epfl', models.CharField(help_text='Utilis\xe9 pour la synchronisation des accr\xe9ditations', max_length=64, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('is_commission', models.BooleanField(default=False, help_text="Cocher si cette unit\xe9 est une commission de l'AGEPoly")),
                ('is_equipe', models.BooleanField(default=False, help_text="Cocher si cette unit\xe9 est une \xe9quipe de l'AGEPoly")),
                ('is_hidden', models.BooleanField(default=False, help_text="Cocher rend l'unit\xe9 inselectionnable au niveau du contexte d'unit\xe9, sauf pour les administrateurs et les personnes accr\xe9dit\xe9es comit\xe9 de l'AGEPoly")),
                ('parent_hierarchique', models.ForeignKey(blank=True, to='units.Unit', help_text="Pour les commissions et les \xe9quipes, s\xe9lectionner le comit\xe9 de l'AGEPoly. Pour les sous-commisions, s\xe9lectionner la commission parente. Pour un coaching de section, s\xe9lectionner la commission Coaching. Pour le comit\xe9 de l'AGEPoly, ne rien mettre.", null=True, on_delete=models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, rights.utils.AgepolyEditableModel, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='UnitLogging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('extra_data', models.TextField(blank=True)),
                ('what', models.CharField(max_length=64, choices=[(b'imported', 'Import\xe9 depuis Truffe 1'), (b'created', 'Creation'), (b'edited', 'Edit\xe9'), (b'deleted', 'Supprim\xe9'), (b'restored', 'Restaur\xe9'), (b'state_changed', 'Statut chang\xe9'), (b'file_added', 'Fichier ajout\xe9'), (b'file_removed', 'Fichier supprim\xe9')])),
                ('object', models.ForeignKey(related_name='logs', to='units.Unit', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(related_name='views', to='units.Unit', on_delete=models.deletion.PROTECT)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='accreditation',
            name='role',
            field=models.ForeignKey(to='units.Role', on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditation',
            name='unit',
            field=models.ForeignKey(to='units.Unit', on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessdelegation',
            name='role',
            field=models.ForeignKey(blank=True, to='units.Role', help_text='(Optionnel !) Le r\xf4le concern\xe9.', null=True, on_delete=models.deletion.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessdelegation',
            name='unit',
            field=models.ForeignKey(to='units.Unit', on_delete=models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessdelegation',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, help_text="(Optionnel !) L'utilisateur concern\xe9. L'utilisateur doit disposer d'une accr\xe9ditation dans l'unit\xe9.", null=True, on_delete=models.deletion.SET_NULL),
            preserve_default=True,
        ),
        migrations.RunPython(initial_values),
    ]
