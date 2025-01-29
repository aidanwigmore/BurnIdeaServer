from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    image = models.ImageField(upload_to='FAQ/')

    def __str__(self):
        return self.question