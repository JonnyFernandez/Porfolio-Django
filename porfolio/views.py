from django.shortcuts import render
from .models import Project


# Create your views here.
def home(req):
    project = Project.objects.all()
    return render(req, "home.html", {"project": project})