from rest_framework import serializers

from .models import About
from drf_extra_fields.fields import Base64ImageField

class AboutSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = About
        fields = '__all__'
