from django.db import models
from ideas.models import Idea
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    visible = models.BooleanField(default=True)
    ideas = models.ManyToManyField(Idea, related_name='ideas')
    category_description = RichTextField()

    color = models.CharField(max_length=100, default='black')

    class QuickConfig:
        name = 'category'
        mutable_fields = [
            'name',
        ]
    