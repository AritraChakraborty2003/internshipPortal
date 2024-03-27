from django.db import models

# Create your models here.
class project(models.Model):
    pid=models.IntegerField()
    project=models.TextField()
    domain=models.TextField()
    duration=models.IntegerField()
class intern(models.Model):
    internId=models.IntegerField()
    pid=models.IntegerField()
    project=models.TextField()
    domain=models.TextField()
    duration=models.IntegerField()