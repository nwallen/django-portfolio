from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartCrop


class FeaturedPortfolio(models.Model):
    portfolio = models.OneToOneField('Portfolio')

    def save(self):
        self.id=1
        super(FeaturedPortfolio, self).save()

    def delete(self):
        pass

    class Meta:
        verbose_name_plural = "Featured Portfolio"
        
    def __unicode__(self):
        return self.portfolio.name


class Portfolio(models.Model):   
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    intro = models.TextField(blank=True, null=True)
    projects = models.ManyToManyField('Project', blank=True)
    public = models.BooleanField()
 
    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    summary = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    people = models.ManyToManyField('Person', blank=True)
    activities = models.ManyToManyField('Activity', blank=True)
    associations = models.ManyToManyField('Association', blank=True)

    def save(self):
        #automatic markdown image syntax completion: ![title] to ![title](url)    
        body = self.description
     
        for media in self.media_set.all():
            imageTag = '![%s]' % media.title
            imageReplace = '![%s](%s)' % (media.title, media.image.url)
            # don't add the url if already added
            exists = body.find(imageReplace)
            if exists == -1:
                self.description = body.replace(imageTag, imageReplace)
        
        super(Project, self).save()

    def __unicode__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "Activities"
    
    def __unicode__(self):
        return self.name
        

class Association(models.Model): 
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
     
    def __unicode__(self):
        return self.name


class Person(models.Model): 
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    position = models.CharField(max_length=50, blank=True);
    url = models.URLField(blank=True, null=True)
     
    class Meta:
        verbose_name_plural = "People"
    
    def __unicode__(self):
        return self.name


class Media(models.Model): 
    project = models.ForeignKey('Project')
    order = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='projectimages', blank=True)
    thumbnail = ImageSpecField ([SmartCrop(50,20)],image_field='image',format='JPEG', options={'quality':90})

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Media"

    def __unicode__(self):
        return self.title
                
