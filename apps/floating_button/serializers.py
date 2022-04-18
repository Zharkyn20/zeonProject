from rest_framework import serializers
from .models import FloatingButton, Callback


class FloatingButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloatingButton
        fields = ('whats_app', 'telegram')


class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = '__all__'
        read_only_fields = ('is_called',)
