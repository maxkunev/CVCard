from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CVProfile(models.Model):
    name = models.CharField(max_length=100, default="Maksym Kuniev")
    position = models.CharField(max_length=200)
    country = models.CharField(max_length=100, default="Sweden")
    email = models.EmailField()
    number = PhoneNumberField()
    linkedin = models.URLField()
    github = models.URLField()
    summary = models.TextField(blank=True, null=True, max_length=1000)   
    class Meta:
        verbose_name = "01. CVProfile"    
        verbose_name_plural = "01. CVProfiles" 
        
    def __str__(self):
        return self.name                                 

class CVSkill(models.Model):
    category = models.CharField(max_length=200)
    technology_stack = models.TextField(max_length=1000) 
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-date_added']
        verbose_name = "02. CVSkill"    
        verbose_name_plural = "02. CVSkills"  
    
    def __str__(self):
        return self.category              

class CVExperience(models.Model):
    title = models.CharField(max_length=200)
    date_start = models.DateField() 
    date_end = models.DateField() 
    description = models.TextField() 
    class Meta:
        ordering = ['date_end']
        verbose_name = "03. CVExperience"    
        verbose_name_plural = "03. CVExperiences"    
    
    def __str__(self):
        return self.title                                                

class CVPetProject(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    github_link = models.URLField(null=True, blank=True) 
    deploy_link = models.URLField(null=True, blank=True) 
    description = models.TextField(max_length=500, null=True, blank=True)
    technology_stack = models.TextField(max_length=1000)
    class Meta:
        ordering = ['-date']
        verbose_name = "04. CVPetProject"    
        verbose_name_plural = "04. CVPetProjects"                                                      

    def __str__(self):
        return self.title 
    
class CVEducation(models.Model):
    title = models.CharField(max_length=200)
    field = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_start = models.DateField() 
    date_end = models.DateField() 
    description = models.TextField() 
    class Meta:
        ordering = ['date_end']
        verbose_name = "05. CVEducation"    
        verbose_name_plural = "05. CVEducations"  
        
    def __str__(self):
        return self.title      

class CVCourses(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField() 
    platform = models.CharField(max_length=200)
    class Meta:
        ordering = ['-date']
        verbose_name = "06. CVCourses"    
        verbose_name_plural = "06. CVCourses"  
        
    def __str__(self):
        return self.title  

    