from rest_framework import serializers
from Contact.models import ContactModel


class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'subject', 'message', 'created')
