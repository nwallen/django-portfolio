from portfolio.models import About, Project, Link, Portfolio, Activity, Video, Photo, Association, Person, FeaturedPortfolio
from django.contrib import admin


class PhotoInline(admin.TabularInline):
    model = Photo

class VideoInline(admin.TabularInline):
    model = Video

class LinkInline(admin.TabularInline):
    model = Link

class AboutAdmin(admin.ModelAdmin):
    model = About
    inlines = [LinkInline]

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ PhotoInline, VideoInline]
    filter_horizontal = ('associations','people','activities')

class PersonAdmin(admin.ModelAdmin):
    model = Person 
    prepopulated_fields = {"slug": ("name",)}


class ActivityAdmin(admin.ModelAdmin):
    model = Activity 
    prepopulated_fields = {"slug": ("name",)}

    
class AssociationAdmin(admin.ModelAdmin):
    model = Association 
    prepopulated_fields = {"slug": ("name",)}


class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'public')
    filter_horizontal = ('projects',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Association, AssociationAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(FeaturedPortfolio)
admin.site.register(About, AboutAdmin)

