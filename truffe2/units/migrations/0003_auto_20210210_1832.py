# Generated by Django 2.2.18 on 2021-02-10 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_auto_20201104_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessdelegation',
            name='access',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('PRESIDENCE', 'Présidence'), ('TRESORERIE', 'Trésorerie'), ('COMMUNICATION', 'Communication'), ('INFORMATIQUE', 'Informatique'), ('ACCREDITATION', 'Accréditations'), ('LOGISTIQUE', 'Logistique'), ('SECRETARIAT', 'Secrétariat'), ('COMMISSIONS', 'Commissions')], max_length=97, null=True),
        ),
        migrations.AlterField(
            model_name='accessdelegation',
            name='role',
            field=models.ForeignKey(blank=True, help_text='(Optionnel !) Le rôle concerné.', null=True, on_delete=django.db.models.deletion.PROTECT, to='units.Role'),
        ),
        migrations.AlterField(
            model_name='accessdelegation',
            name='user',
            field=models.ForeignKey(blank=True, help_text="(Optionnel !) L'utilisateur concerné. L'utilisateur doit disposer d'une accréditation dans l'unité.", null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accessdelegationlogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='accessdelegationlogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accessdelegationviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accreditation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accreditationlog',
            name='type',
            field=models.CharField(choices=[('created', 'Créée'), ('edited', 'Modifiée'), ('deleted', 'Supprimée'), ('autodeleted', 'Supprimée automatiquement'), ('renewed', 'Renouvelée'), ('validated', 'Validée'), ('autocreated', 'Créée automatiquement')], max_length=32),
        ),
        migrations.AlterField(
            model_name='accreditationlog',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role',
            name='access',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('PRESIDENCE', 'Présidence'), ('TRESORERIE', 'Trésorerie'), ('COMMUNICATION', 'Communication'), ('INFORMATIQUE', 'Informatique'), ('ACCREDITATION', 'Accréditations'), ('LOGISTIQUE', 'Logistique'), ('SECRETARIAT', 'Secrétariat'), ('COMMISSIONS', 'Commissions')], max_length=97, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(default='---', max_length=255),
        ),
        migrations.AlterField(
            model_name='rolelogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='rolelogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roleviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(default='---', max_length=255),
        ),
        migrations.AlterField(
            model_name='unit',
            name='parent_hierarchique',
            field=models.ForeignKey(blank=True, help_text="Pour les commissions et les équipes, sélectionner le comité de l'AGEPoly. Pour les sous-commisions, sélectionner la commission parente. Pour un coaching de section, sélectionner la commission Coaching. Pour le comité de l'AGEPoly, ne rien mettre.", null=True, on_delete=django.db.models.deletion.PROTECT, to='units.Unit'),
        ),
        migrations.AlterField(
            model_name='unitlogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='unitlogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unitviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
