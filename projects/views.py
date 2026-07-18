from django.shortcuts import get_object_or_404, render
from main.models import CVPetProject
from projects.models import ProjectsInfo

# Create your views here.

def projects(request):
    projects = CVPetProject.objects.all()
    context = {'cvpetprojects': projects}
    return render(request, 'projects/projects.html', context = context)

def project(request, project_id):
    project = get_object_or_404(CVPetProject.objects.prefetch_related('info'), id=project_id)
    information = project.info.all().order_by('order')
    context = {
        'project': project,
        'information': information
    }
    return render(request, 'projects/project.html', context = context)