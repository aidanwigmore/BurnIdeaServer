from rest_framework import serializers

from .models import Idea, Category
from ideas.serializers import IdeaSerializer

class CategorySerializer(serializers.ModelSerializer):
    ideas = serializers.PrimaryKeyRelatedField(queryset=Idea.objects.all(), many=True)    
    
    class Meta:
        model = Category
        fields = '__all__'

    def update(self, instance, validated_data):
        ideas = validated_data.pop('ideas', None)
        instance = super().update(instance, validated_data)
        if ideas is not None:
            instance.ideas.set(ideas)
        return instance

    