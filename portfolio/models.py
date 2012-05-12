from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartCrop

class Project(models.Model):
    name = models.CharField(max_length=200);
    slug = models.SlugField(max_length=50, unique=True)
    summary = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    activities = models.ManyToManyField('Activity', blank=True)
    associations = models.ManyToManyField('Association', blank=True)

    def __unicode__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=50);
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "Activities"
    
    def __unicode__(self):
        return self.name
        

class Association(models.Model): 
    name = models.CharField(max_length=50);
    slug = models.SlugField(max_length=50, unique=True)
     
    def __unicode__(self):
        return self.name


class Media(models.Model): 
    project = models.ForeignKey('Project')
    order = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(blank=True, null=True);
    image = models.ImageField(upload_to='projectimages', blank=True)
    thumbnail = ImageSpecField ([SmartCrop(50,20)],image_field='image',format='JPEG', options={'quality':90})

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Media"

    def __unicode__(self):
        return self.title
                
