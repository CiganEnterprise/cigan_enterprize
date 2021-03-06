from django.contrib import admin

from .models import Studio, Employer, Project


class StudioAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'country', 'moment')
    prepopulated_fields = {'studio_slug': ('city',)}


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'post', 'experience')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name_of_project', 'field')


admin.site.register(Studio, StudioAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Project, ProjectAdmin)

admin.site.site_header = "CiganEnterprize administration board"

