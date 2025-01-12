from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    image = models.ImageField(upload_to='FAQ/', blank=True, null=True)

    def __str__(self):
        return self.question