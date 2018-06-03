from django.shortcuts import render
from django.http import HttpResponse

from .models import Featurette

# Create your views here.
def index(request):
    context = {
        "featurettes": Featurette.objects.all(),
        "nbar": "index"
    }
    return render(request, "portfolio/index.html", context)
