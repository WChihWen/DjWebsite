from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DjangoProject(models.Model):
    djangoprojectTitle = models.CharField(max_length=255)
    djangoprojectUrl = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.djangoprojectTitle
    
    class Meta:
        db_table='djangoproject'

class Courses(models.Model):
    courseTitle = models.CharField(max_length=255)
    courseSubject = models.CharField(max_length=255)
    courseCatalog = models.IntegerField()
    courseTerm = models.CharField(max_length=255)
    courseUnits = models.FloatField()
    courseInstructor = models.CharField(max_length=255)
    courseGrades = models.FloatField()
    
    def __str__(self):
        return self.courseTitle
    
    class Meta:
        db_table='courses'
        
