from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("projects", views.projects, name='projects'),
    path("experience", views.experience, name='experience'),
    path("education", views.education, name='education'),
    path("resume", views.resume, name='resume'),
    path("transcript", views.transcript,  name='transcript'),
]
