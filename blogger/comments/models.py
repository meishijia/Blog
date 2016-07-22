from __future__ import unicode_literals

from django.db import models

from articles.models import Article
from django.contrib.auth.models import User

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    article = models.ForeignKey(Article,on_delete = models.CASCADE)
    





# Create your models here.
