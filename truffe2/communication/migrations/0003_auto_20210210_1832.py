# Generated by Django 2.2.18 on 2021-02-10 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_auto_20201104_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agepslide',
            name='picture',
            field=models.ImageField(help_text="Pour des raisons de qualité, il est fortement recommandé d'envoyer une image en HD (1920x1080)", upload_to='uploads/slides/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='agepslide',
            name='status',
            field=models.CharField(choices=[('0_draft', 'Brouillon'), ('1_asking', 'Modération en cours'), ('2_online', 'En ligne'), ('3_archive', 'Archivé'), ('4_deny', 'Refusé'), ('4_canceled', 'Annulé')], default='0_draft', max_length=255),
        ),
        migrations.AlterField(
            model_name='agepslidelogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='agepslidelogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agepslideviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='displaylogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='displaylogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='displayreservation',
            name='status',
            field=models.CharField(choices=[('0_draft', 'Brouillon'), ('1_asking', 'Validation en cours'), ('2_online', 'Validé'), ('3_archive', 'Archivé'), ('4_deny', 'Refusé'), ('4_canceled', 'Annulé')], default='0_draft', max_length=255),
        ),
        migrations.AlterField(
            model_name='displayreservationlogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='displayreservationlogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='displayreservationviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='displayviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='logo',
            name='name',
            field=models.CharField(default='---', max_length=255),
        ),
        migrations.AlterField(
            model_name='logo',
            name='visibility_level',
            field=models.CharField(choices=[('default', "De base (En fonction de l'objet et des droits)"), ('unit', 'Unité liée'), ('unit_agep', "Unité liée et Comité de l'AGEPoly"), ('all_agep', 'Toutes les personnes accrédités dans une unité'), ('all', 'Tout le monde')], default='default', help_text="Permet de rendre l'objet plus visible que les droits de base", max_length=32, verbose_name='Visibilité'),
        ),
        migrations.AlterField(
            model_name='logofile',
            name='file',
            field=models.FileField(upload_to='uploads/_generic/Logo/'),
        ),
        migrations.AlterField(
            model_name='logofile',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='logologging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='logologging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='logoviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='websitenews',
            name='status',
            field=models.CharField(choices=[('0_draft', 'Brouillon'), ('1_asking', 'Modération en cours'), ('2_online', 'En ligne'), ('3_archive', 'Archivé'), ('4_deny', 'Refusé'), ('4_canceled', 'Annulé')], default='0_draft', max_length=255),
        ),
        migrations.AlterField(
            model_name='websitenewslogging',
            name='what',
            field=models.CharField(choices=[('imported', 'Importé depuis Truffe 1'), ('created', 'Creation'), ('edited', 'Edité'), ('deleted', 'Supprimé'), ('restored', 'Restauré'), ('state_changed', 'Statut changé'), ('file_added', 'Fichier ajouté'), ('file_removed', 'Fichier supprimé')], max_length=64),
        ),
        migrations.AlterField(
            model_name='websitenewslogging',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='websitenewsviews',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
