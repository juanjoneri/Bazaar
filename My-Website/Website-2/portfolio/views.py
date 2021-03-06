from django.shortcuts import render
from django.http import HttpResponse

from .models import Featurette, Project, Experience

# Create your views here.
def index(request):
    context = {
        "featurettes": Featurette.objects.all(),
        "nbar": "index"
    }
    return render(request, "portfolio/index.html", context)


def experience(request):
    context = {
        "experiences": Experience.objects.order_by('from_date').reverse(),
        "nbar": "experience"
    }
    return render(request, "portfolio/experience.html", context)


def projects(request):
    context = {
        "projects": Project.objects.all(),
        "nbar": "projects"
    }
    return render(request, "portfolio/projects.html", context)

def education(request):
    return render(request, "portfolio/education.html", context={"nbar": "education"})