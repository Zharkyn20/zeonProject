from rest_framework import serializers
from .models import AboutUs, AboutUsImage


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ('image',)


class AboutUsSerializer(serializers.ModelSerializer):
    # get images for AboutUs
    image = AboutUsImageSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = '__all__'
