# -*- coding: utf-8 -*-

from django.forms import ModelForm, Form, CharField, ChoiceField, Textarea, BooleanField, ValidationError
from django.utils.translation import ugettext_lazy as _

from app.utils import get_property


class GenericForm(ModelForm):

    class Meta:
        pass

    def __init__(self, current_user, *args, **kwargs):
        from users.models import TruffeUser
        from units.models import Unit

        super(GenericForm, self).__init__(*args, **kwargs)

        if 'user' in self.fields:
            if hasattr(self.Meta.model.MetaData, 'has_unit') and self.Meta.model.MetaData.has_unit:
                if hasattr(self.Meta.model, 'MetaEdit') and hasattr(self.Meta.model.MetaEdit, 'all_users') and self.Meta.model.MetaEdit.all_users:
                    self.fields['user'].queryset = TruffeUser.objects.all()  # Some classes allow creation of instances for any user (NdF, JdC)
                else:
                    unit = get_property(self.instance, self.instance.MetaRights.linked_unit_property) if get_property(self.instance, 'MetaRights.linked_unit_property') else self.instance.unit
                    self.fields['user'].queryset = TruffeUser.objects.filter(accreditation__unit=unit, accreditation__end_date=None).distinct().order_by('first_name', 'last_name')

        if 'unit' in self.fields:
            self.fields['unit'].queryset = Unit.objects.order_by('name')

        if hasattr(self.Meta.model, 'MetaEdit') and hasattr(self.Meta.model.MetaEdit, 'only_if'):
            for key, test in self.Meta.model.MetaEdit.only_if.items():
                if not test(self.instance, current_user):
                    if key in self.fields:
                        del self.fields[key]

        if hasattr(self.instance, 'genericFormExtraInit'):
            self.instance.genericFormExtraInit(self, current_user, *args, **kwargs)

    def clean(self):
        cleaned_data = super(GenericForm, self).clean()

        if hasattr(self.instance, 'genericFormExtraClean'):
            self.instance.genericFormExtraClean(cleaned_data, self)

        if hasattr(self.instance, 'genericFormExtraCleanWithLines'):
            self.instance.genericFormExtraCleanWithLines(cleaned_data, self, self._clean_line_data)

        from rights.utils import UnitExternalEditableModel

        if isinstance(self.instance, UnitExternalEditableModel):
            if not self.instance.unit and not cleaned_data['unit_blank_name']:
                self._errors["unit_blank_name"] = self.error_class([_(u"Le nom de l'entité externe est obligatoire !")])  # Until Django 1.6
                # self.add_error("unit_blank_name", _(u"Le nom de l'entité externe est obligatoire !"))  # From Django 1.7

        from accounting_core.utils import CostCenterLinked

        if 'costcenter' in self.fields and issubclass(self.Meta.model, CostCenterLinked):
            if 'costcenter' not in cleaned_data:
                raise ValidationError(_(u'Aucun centre de coûts sélectionné !'))

            if hasattr(self.instance, 'unit'):
                list_unit_pk = [self.instance.unit.pk] + [un.pk for un in self.instance.unit.sub_eqi() + self.instance.unit.sub_grp()]
                if cleaned_data['costcenter'].unit.pk not in list_unit_pk:
                    raise ValidationError(_(u'Le centre de coût n\'est pas lié à l\'unité !'))

            if hasattr(self.instance, 'accounting_year') and self.instance.accounting_year != cleaned_data['costcenter'].accounting_year:
                raise ValidationError(_(u'Le centre de coût n\'est pas lié à l\'année comptable !'))

        return cleaned_data


class ContactForm(Form):

    subject = CharField(label=_('Sujet'), max_length=100)
    message = CharField(label=_('Message'), widget=Textarea)
    receive_copy = BooleanField(label=_('Recevoir une copie?'), required=False, initial=True)

    def __init__(self, keys, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        choices_key = [x for x in keys.items()]

        self.fields['key'] = ChoiceField(label=_('Destinataire(s)'), choices=choices_key)
