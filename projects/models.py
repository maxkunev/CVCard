from django.db import models

from main.models import CVPetProject

# Create your models here.

from django.utils.text import slugify
import os

def project_image_path(instance, filename):
    clean_path = slugify(instance.project.title)
    return f"projectsimg/{clean_path}/{filename}"

class ProjectsInfo(models.Model):
    project = models.ForeignKey(CVPetProject, on_delete=models.CASCADE, related_name="info")
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=project_image_path, blank=True, null=True)
    order = models.PositiveIntegerField()
    class Meta:
        ordering = ["order"]
    