from django.shortcuts import get_object_or_404, render, redirect
from main.models import *
from django.contrib import messages
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60*60*24)
def index(request):
    
    cvprofile = CVProfile.objects.all().first()
    cvskills = CVSkill.objects.all()    
    cvexperiences = CVExperience.objects.all()    
    cvpetprojects = CVPetProject.objects.all()
    cveducations = CVEducation.objects.all()
    cvcourses = CVCourses.objects.all()
    
    context = {
        "cvprofile":cvprofile,
        "cvskills":cvskills,
        "cvexperiences":cvexperiences,
        "cvpetprojects":cvpetprojects,
        "cveducations":cveducations,
        "cvcourses":cvcourses
    }
    
    return render(request, "main/index.html", context=context)