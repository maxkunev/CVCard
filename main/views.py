from django.shortcuts import get_object_or_404, render, redirect
from main.models import *
from django.contrib import messages
from django.core.cache import cache
from django.contrib import messages

# Create your views here.

def index(request):
    cvprofile = cache.get("cvprofile")
    if not cvprofile:
        cvprofile = CVProfile.objects.first()
        cache.set("cvprofile", cvprofile, 60 * 60 * 24)

    cvskills = cache.get("cvskills")
    if not cvskills:
        cvskills = list(CVSkill.objects.all())
        cache.set("cvskills", cvskills, 60 * 60 * 24)

    cvexperiences = cache.get("cvexperiences")
    if not cvexperiences:
        cvexperiences = list(CVExperience.objects.all())
        cache.set("cvexperiences", cvexperiences, 60 * 60 * 24)

    cvpetprojects = cache.get("cvpetprojects")
    if not cvpetprojects:
        cvpetprojects = list(CVPetProject.objects.all())
        cache.set("cvpetprojects", cvpetprojects, 60 * 60 * 24)

    cveducations = cache.get("cveducations")
    if not cveducations:
        cveducations = list(CVEducation.objects.all())
        cache.set("cveducations", cveducations, 60 * 60 * 24)

    cvcourses = cache.get("cvcourses")
    if not cvcourses:
        cvcourses = list(CVCourses.objects.all())
        cache.set("cvcourses", cvcourses, 60 * 60 * 24)
    
    context = {
        "cvprofile":cvprofile,
        "cvskills":cvskills,
        "cvexperiences":cvexperiences,
        "cvpetprojects":cvpetprojects,
        "cveducations":cveducations,
        "cvcourses":cvcourses
    }
    
    return render(request, "main/index.html", context=context)

def projects(request):
    messages.info(request, "Projects currently unavailable. Work in progress...")
    return redirect("main:index")

def contact(request):
    messages.info(request, "Contact form currently unavailable. Work in progress....")
    return redirect("main:index")