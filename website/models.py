from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
"""
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_prof = models.BooleanField('Is prof', default=False)
    is_student = models.BooleanField('Is student', default=False)
"""

class branch1(models.Model):
    sno = models.IntegerField()
    mon = models.CharField(max_length=25, blank=True)
    tue = models.CharField(max_length=25, blank=True)
    wed = models.CharField(max_length=25, blank=True)
    thu = models.CharField(max_length=25, blank=True)
    fri = models.CharField(max_length=25, blank=True)

class branch2(models.Model):
    sno = models.IntegerField()
    mon = models.CharField(max_length=25, blank=True)
    tue = models.CharField(max_length=25, blank=True)
    wed = models.CharField(max_length=25, blank=True)
    thu = models.CharField(max_length=25, blank=True)
    fri = models.CharField(max_length=25, blank=True)

class branch3(models.Model):
    sno = models.IntegerField()
    mon = models.CharField(max_length=25, blank=True)
    tue = models.CharField(max_length=25, blank=True)
    wed = models.CharField(max_length=25, blank=True)
    thu = models.CharField(max_length=25, blank=True)
    fri = models.CharField(max_length=25, blank=True)

class prof(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=25)
    branches = models.CharField(max_length=50)

