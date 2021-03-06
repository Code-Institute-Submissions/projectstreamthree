from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings


# Code taken from Code Institute lesson
class Subject(models.Model):
    """Subject model requiring a name and description"""
    name = models.CharField(max_length=255)
    description = HTMLField()

    def __unicode__(self):
        return self.name


# Code taken from Code Institute lesson
class Thread(models.Model):
    """A thread being related to it's subject"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)


# Code taken from Code Institute lesson
class Post(models.Model):
    """A post being related to it's thread"""
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
