from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField()

# Create your models here.
