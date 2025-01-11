from rest_framework import serializers
from .models import Idea
from drf_extra_fields.fields import Base64ImageField

class IdeaSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Idea
        fields = '__all__'

    