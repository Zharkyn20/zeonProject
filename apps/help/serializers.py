from rest_framework import serializers
from .models import Help, HelpDetails


class HelpDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpDetails
        fields = ('question', 'answer')


class HelpSerializer(serializers.ModelSerializer):
    help = HelpDetailsSerializer(many=True)

    class Meta:
        model = Help
        fields = '__all__'
