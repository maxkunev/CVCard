from django.urls import path, include
from projects import views

app_name = "projects"

urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('project/<int:project_id>', views.project, name='project'),
    ]