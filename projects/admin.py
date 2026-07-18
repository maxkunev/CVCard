from django.contrib import admin
from projects.models import ProjectsInfo
# Register your models here.

class ProjectsInfoAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', "project", "order")
    ordering = ['project', 'order']


admin.site.register(ProjectsInfo, ProjectsInfoAdmin)