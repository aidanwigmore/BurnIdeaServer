from django.db import models

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=100)
    idea_description = models.TextField()

    idea_difficulty = models.IntegerField()

    visible = models.BooleanField(default=True)
    
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class QuickConfig:
        name = 'idea'
        mutable_fields = [
            'name',
        ]
    