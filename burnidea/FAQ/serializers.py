from rest_framework import serializers

from .models import FAQ
from drf_extra_fields.fields import Base64ImageField

class FAQSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = FAQ
        fields = '__all__'
