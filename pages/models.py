from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Teams(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    designation = models.CharField(max_length=30)
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=30)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Team'

    def __str__(self):
        return self.first_name+' '+self.last_name
