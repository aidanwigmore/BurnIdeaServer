from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class FAQ(models.Model):
    question = RichTextField()
    answer = RichTextField()

    image = models.ImageField(upload_to='FAQ/', blank=True, null=True)

    def __str__(self):
        return self.question