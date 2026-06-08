from django.urls import path, include
from main import views

app_name = "main"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact')
    ]