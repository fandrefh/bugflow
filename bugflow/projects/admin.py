from django.contrib import admin

from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'started_at', 'finished_at', 'objective', 'user']


admin.site.register(Project, ProjectAdmin)
