from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=100)
    idea_description = RichTextField()

    idea_difficulty = models.IntegerField()

    visible = models.BooleanField(default=True)
    
    image = models.ImageField(upload_to='ideas/', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    class QuickConfig:
        name = 'idea'
        mutable_fields = [
            'name',
        ]
    