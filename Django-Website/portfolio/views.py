from django.shortcuts import render
from django.http import HttpResponse

from .models import Featurette, Project, Experience, Visit

# Create your views here.
def index(request):
    # register the Visit
    ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR')).split(',')[-1].strip()
    visit = Visit(ip=str(ip))
    visit.save()
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

def resume(request):
    with open('./portfolio/static/portfolio/doc/CV.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=resume.pdf'
        return response

def transcript(request):
    with open('./portfolio/static/portfolio/doc/Transcript.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=transcript.pdf'
        return response
