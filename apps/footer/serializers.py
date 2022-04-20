from rest_framework import serializers
from .models import Footer, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact', 'link')


class FooterSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Footer
        fields = ('phone', 'icon', 'text', 'contacts')
