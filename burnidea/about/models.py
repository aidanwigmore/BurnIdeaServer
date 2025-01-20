from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    content = RichTextField()
    visible = models.BooleanField(default=True)
    
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.content