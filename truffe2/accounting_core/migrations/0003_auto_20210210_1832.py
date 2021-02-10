# Generated by Django 2.2.18 on 2021-02-10 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_core', '0002_auto_20201104_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default='---', max_length=255, verbose_name='Nom du compte'),
        ),
        migrations.AlterField(
            model_name='account',
            name='visibility',
            field=models.CharField(choices=[('all', 'Visible à tous'), ('cdd', 'Visible au Comité de Direction uniquement'), ('root', 'Visible aux personnes qui gère la comptabilité générale'), ('none', 'Visible à personne')], max_length=50, verbose_name='Visibilité dans les documents comptables'),
        ),
        migrations.AlterField(
            model_name='accountcategory',
            name='name',
            field=models.CharField(default='---', max_length=255, verbose_name='Nom de la catégorie'),
        ),
        migrations.AlterField(
            model_name='accountcategory',
            name='parent_hierarchique',
            field=models.ForeignKey(blank=True, help_text='Catégorie parente pour la hiérarchie', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting_core.AccountCategory'),
        ),
        migrations.AlterField(
            model_name='accountcategorylogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='accountcategorylogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountcategoryviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountingyear',
            name='name',
            field=models.CharField(default='---', max_length=255, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='accountingyear',
            name='status',
            field=models.CharField(choices=[('0_preparing', 'En préparation'), ('1_active', 'Année active'), ('2_closing', 'En clôture'), ('3_archived', 'Année archivée')], default='0_preparing', max_length=255),
        ),
        migrations.AlterField(
            model_name='accountingyearlogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='accountingyearlogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountingyearviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountlogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='accountlogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='costcenter',
            name='name',
            field=models.CharField(default='---', max_length=255, verbose_name='Nom du centre de coût'),
        ),
        migrations.AlterField(
            model_name='costcenterlogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='costcenterlogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='costcenterviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tva',
            name='name',
            field=models.CharField(default='---', max_length=255, verbose_name='Nom de la TVA'),
        ),
        migrations.AlterField(
            model_name='tvalogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='tvalogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tvaviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
