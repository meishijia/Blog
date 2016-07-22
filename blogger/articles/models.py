from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length = 30)
    time_stamp = models.DateField()
    content = models.TextField()
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    
# Create your models here.