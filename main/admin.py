from django.contrib import admin
from main.models import *
# Register your models here.


class CVProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    
class CVSkillAdmin(admin.ModelAdmin):
    list_display = ("id", "category")
    
class CVExperienceAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    
class CVPetProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    
class CVEducationAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    
class CVCoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(CVProfile, CVProfileAdmin)
admin.site.register(CVSkill)
admin.site.register(CVExperience)
admin.site.register(CVPetProject)
admin.site.register(CVEducation)
admin.site.register(CVCourses)
