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
admin.site.register(CVSkill, CVSkillAdmin)
admin.site.register(CVExperience, CVExperienceAdmin)
admin.site.register(CVPetProject, CVPetProjectAdmin)
admin.site.register(CVEducation, CVEducationAdmin)
admin.site.register(CVCourses, CVCoursesAdmin)
