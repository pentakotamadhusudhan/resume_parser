from  rest_framework import serializers
from .models import *

class ImageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploadModel
        fields = '__all__'

class VideoCameraSerializer(serializers.Serializer):
    status = serializers.BooleanField()