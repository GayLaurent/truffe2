# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateInput
from django.utils.translation import gettext_lazy as _

from accounting_tools.models import InvoiceLine, SubventionLine


class InvoiceLineForm(ModelForm):

    class Meta:
        model = InvoiceLine
        exclude = ('invoice', 'order',)


class SubventionLineForm(ModelForm):

    class Meta:
        model = SubventionLine
        exclude = ('subvention', 'order')

        widgets = {
            'start_date': DateInput(attrs={'class': 'datepicker'}),
            'end_date': DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker'}),
        }
