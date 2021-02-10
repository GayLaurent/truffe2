# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import generic.search
import rights.utils


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruffeUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=255, verbose_name='Sciper ou username')),
                ('first_name', models.CharField(max_length=100, verbose_name='Pr\xe9nom', blank=True)),
                ('last_name', models.CharField(max_length=100, verbose_name='Nom de famille', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='Adresse email')),
                ('email_perso', models.EmailField(max_length=255, null=True, verbose_name='Adresse email priv\xe9e', blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='D\xe9fini si cet utilisateur doit \xeatre consid\xe9r\xe9 comme actif. D\xe9sactiver ceci au lieu de supprimer le compte.', verbose_name='Actif')),
                ('is_betatester', models.BooleanField(default=False, help_text='Rend visible les \xe9l\xe9ments en cours de d\xe9veloppement', verbose_name='Betatesteur')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'inscription")),
                ('mobile', models.CharField(max_length=25, blank=True)),
                ('adresse', models.TextField(blank=True)),
                ('nom_banque', models.CharField(help_text='Pour la poste, mets Postfinance. Sinon, mets le nom de ta banque.', max_length=128, blank=True)),
                ('iban_ou_ccp', models.CharField(help_text='Pour la poste, mets ton CCP. Sinon, mets ton IBAN', max_length=128, blank=True)),
                ('body', models.CharField(default=b'.', max_length=1)),
                ('homepage', models.TextField(null=True, blank=True)),
                ('avatar', models.ImageField(help_text='Si pas renseign\xe9, utilise la photo EPFL. Si pas de photo EPFL publique, utilise un poney.', null=True, upload_to=b'uploads/avatars/', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=(models.Model, rights.utils.ModelWithRight, generic.search.SearchableModel),
        ),
        migrations.CreateModel(
            name='UserPrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field', models.CharField(max_length=64, choices=[(b'mobile', 'Mobile'), (b'adresse', 'Adresse'), (b'nom_banque', 'Nom banque'), (b'iban_ou_ccp', 'IBAN ou CCP'), (b'email_perso', 'Adresse email priv\xe9e')])),
                ('level', models.CharField(max_length=64, choices=[(b'prive', 'Priv\xe9'), (b'groupe', 'Membres de mes groupes'), (b'member', 'Accr\xe9dit\xe9s AGEPoly'), (b'public', 'Public')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
