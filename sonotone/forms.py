from django import forms

from django.utils.translation import ugettext_lazy as _
from sonotone.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

#    email = forms.EmailField(required=True, label=_('Ton adresse e-mail'))
#    firstname = forms.CharField(required=True, max_length=64, label=_('Prenom'))
#    surname = forms.CharField(required=True, max_length=64, label=_('Nom de famille'))