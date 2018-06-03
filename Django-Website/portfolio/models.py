from django.db import models

# Create your models here.
class Featurette(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    link = models.URLField()

    def __str__(self):
        return f'{self.title}'
