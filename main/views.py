from django.shortcuts import get_object_or_404, render, redirect
from main.models import *
from django.contrib import messages
from django.core.cache import cache
from django.contrib import messages

# Create your views here.

def index(request):
    context = cache.get("cv_full_context")
    
    if not context:
        context = {
            "cvprofile": CVProfile.objects.first(),
            "cvskills": list(CVSkill.objects.all()),
            "cvexperiences": list(CVExperience.objects.all()),
            "cvpetprojects": list(CVPetProject.objects.all()),
            "cveducations": list(CVEducation.objects.all()),
            "cvcourses": list(CVCourses.objects.all()),
        }
        cache.set("cv_full_context", context, 60 * 60 * 24)
    
    return render(request, "main/index.html", context=context)

def projects(request):
    messages.info(request, "Projects currently unavailable. Work in progress...")
    return redirect("main:index")

def contact(request):
    messages.info(request, "Contact form currently unavailable. Work in progress....")
    return redirect("main:index")