from django.db import models

# Create your models here.
class Featurette(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    link = models.URLField()
    button = models.CharField(max_length=8)
    img = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title}'
