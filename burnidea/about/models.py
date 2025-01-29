from django.db import models

# Create your models here.
class About(models.Model):
    content = models.TextField()
    visible = models.BooleanField(default=True)
    
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.content