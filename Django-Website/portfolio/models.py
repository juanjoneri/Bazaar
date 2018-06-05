from django.db import models
import django

from datetime import datetime
# Create your models here.

class Visit(models.Model):
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip = models.CharField(max_length=32)

    def __str__(self):
        return "{} @ {}".format(self.ip, self.date)

class Featurette(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    link = models.URLField()
    button = models.CharField(max_length=8)
    img = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    link = models.URLField()
    button_icon = models.CharField(max_length=32)
    img = models.CharField(max_length=64)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    location = models.CharField(max_length=32)
    icon = models.CharField(max_length=32, default="fas fa-sun")

    def __str__(self):
        return self.title
