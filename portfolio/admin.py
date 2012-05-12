from portfolio.models import Project
from portfolio.models import Activity
from portfolio.models import Media
from portfolio.models import Association
from django.contrib import admin


class MediaInline(admin.TabularInline):
    model = Media


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ MediaInline,]


class ActivityAdmin(admin.ModelAdmin):
    model = Activity 
    prepopulated_fields = {"slug": ("name",)}
    

class AssociationAdmin(admin.ModelAdmin):
    model = Association 
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Association, AssociationAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)
