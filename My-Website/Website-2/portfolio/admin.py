from django.contrib import admin

# Register your models here.
from .models import Featurette, Project, Experience

admin.site.register(Featurette)
admin.site.register(Project)
admin.site.register(Experience)
