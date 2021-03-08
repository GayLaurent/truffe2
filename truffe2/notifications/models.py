from django.db import models
from django.db.models.deletion import PROTECT, PROTECT
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.conf import settings
from django.utils.translation import gettext_lazy as _

import json


class Notification(models.Model):
    key = models.CharField(max_length=255)

    species = models.CharField(max_length=255)

    creation_date = models.DateTimeField(auto_now_add=True)
    seen_date = models.DateTimeField(blank=True, null=True)

    seen = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=PROTECT)
    object_id = models.PositiveIntegerField()
    linked_object = fields.GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)

    metadata = models.TextField(blank=True, null=True)

    def set_metadata(self, data):
        self.metadata = json.dumps(data)

    def get_metadata(self):
        return json.loads(self.metadata)

    def get_template(self):
        return 'notifications/species/%s.html' % (self.species,)

    def get_email_template(self):
        return 'notifications/species/mails/%s.html' % (self.species,)

    def get_center_message_template(self):
        return 'notifications/species/center/message/%s.html' % (self.species,)

    def get_center_buttons_template(self):
        return 'notifications/species/center/buttons/%s.html' % (self.species,)


class NotificationRestriction(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    key = models.CharField(max_length=255)

    no_email = models.BooleanField(default=False)
    autoread = models.BooleanField(default=False)
    no_email_group = models.BooleanField(default=False, help_text=_(u'Ne pas regrouper les notification en un seul mail'))


class NotificationEmail(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    notification = models.ForeignKey(Notification, on_delete=PROTECT)
    no_email_group = models.BooleanField(default=False, help_text=_(u'Ne pas regrouper les notification en un seul mail'))
