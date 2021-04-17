from django.db import models

# Create your models here.
class Project(models.Model):
    index = models.IntegerField(blank=True, default=0)
    
    title = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    thumbnail = models.ImageField(blank=True)
    
    
    text1 = models.CharField(max_length=200, blank=True)
    image1 = models.ImageField(blank=True)
         
    text2 = models.CharField(max_length=200, blank=True)
    image2 = models.ImageField(blank=True)
         
    text3 = models.CharField(max_length=200, blank=True)
    image3 = models.ImageField(blank=True)
         
    text4 = models.CharField(max_length=200, blank=True)
    image4 = models.ImageField(blank=True)
         
    text5 = models.CharField(max_length=200, blank=True)
    image5 = models.ImageField(blank=True)
         
    text6 = models.CharField(max_length=200, blank=True)
    image6 = models.ImageField(blank=True)
         
    text7 = models.CharField(max_length=200, blank=True)
    image7 = models.ImageField(blank=True)
              
    text8 = models.CharField(max_length=200, blank=True)
    image8 = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title