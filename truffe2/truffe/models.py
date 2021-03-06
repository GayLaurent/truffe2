from django.db import models
from django.conf import settings
from django.db.models.deletion import PROTECT, PROTECT

class ImportedCreditCard(models.Model):
    name = models.CharField(max_length=255, unique=True, default='---')
    description = models.TextField()
    amount = models.IntegerField()
    card_date = models.DateField()
    status = models.CharField(max_length=255)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    costcenter_id = models.PositiveIntegerField()
    accounting_year_id = models.PositiveIntegerField()
