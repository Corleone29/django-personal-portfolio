from typing import Any
from django.shortcuts import render
from .models import Project

def home(request: Any):
    projects = Project.objects.all() # grabs objects from database
    return render(request, 'portfolio/home.html', {'projects':projects})
