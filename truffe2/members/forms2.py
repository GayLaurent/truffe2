# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext_lazy as _

from members.models import Membership
from users.models import TruffeUser

import re


class MembershipAddForm(forms.ModelForm):

    user = forms.CharField()

    class Meta:
        model = Membership
        exclude = ('start_date', 'end_date', 'user', 'group')

    def __init__(self, current_user, group, *args, **kwargs):
        """"""
        super(MembershipAddForm, self).__init__(*args, **kwargs)

        if not group or not group.handle_fees:
            del self.fields['payed_fees']

    def clean_user(self):
        data = self.cleaned_data['user']
        if not re.match(r'^\d{6}$', data):
            try:
                TruffeUser.objects.get(username=data)
            except TruffeUser.DoesNotExist:
                raise forms.ValidationError(_('Pas un username valide'))

        return data

    def clean(self):
        cleaned_data = super(MembershipAddForm, self).clean()

        if cleaned_data.get('generates_accred') and cleaned_data.get('generated_accred_type') is None:
            raise forms.ValidationError(u"Le type d'accréditation généré ne peut pas avoir un type nul si une accréditation est générée.")

        return cleaned_data


class MembershipImportForm(forms.Form):

    imported = forms.FileField(label=_(u'Fichier à importer'))
    copy_fees_status = forms.BooleanField(label=_(u'Copier les cotisations ?'), required=False)

    def __init__(self, current_user, group, *args, **kwargs):
        """"""
        super(MembershipImportForm, self).__init__(*args, **kwargs)

        self.fields['imported'].help_text = _(u'Accepte les fichiers JSON composés de listes de username ou de listes de couples (username, cotisation_payée)')

        if not group or not group.handle_fees:
            del self.fields['copy_fees_status']


class MembershipImportListForm(forms.Form):
    data = forms.CharField(label=_(u'Liste de scipers, un par ligne'), widget=forms.Textarea)
    fee_status = forms.BooleanField(label=_(u'Définir les cotisations comme payée ?'), required=False)
