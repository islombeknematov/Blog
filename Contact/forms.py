from django import forms
from Contact.models import ContactModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'email', 'subject', 'message']
        model = ContactModel
