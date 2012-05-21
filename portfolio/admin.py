from portfolio.models import Project, Portfolio, Activity, Media, Association, Person, FeaturedPortfolio
from django.contrib import admin


class MediaInline(admin.TabularInline):
    model = Media


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ MediaInline,]
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
