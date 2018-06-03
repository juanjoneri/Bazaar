from django.shortcuts import render
from django.http import HttpResponse

from .models import Featurette, Project

# Create your views here.
def index(request):
    context = {
        "featurettes": Featurette.objects.all(),
        "nbar": "index"
    }
    return render(request, "portfolio/index.html", context)

def projects(request):
    context = {
        "projects": Project.objects.all(),
        "nbar": "projects"
    }
    return render(request, "portfolio/projects.html", context)
