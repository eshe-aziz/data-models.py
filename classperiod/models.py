from django.db import models

# Create your models here.


class Class_Period(models.Model):
    starttime = models.TimeField()
    endtime = models.TimeField()
    course = models.CharField(max_length= 200)
    classroom = models.CharField(max_length=50)
    dayoftheweek = models.CharField(max_length=20)
    duration = models.IntegerField()
    syllabus = models.TextField()
    capacity = models.IntegerField()
    attendance = models.ManyToManyField()


def __str__(self):
    return f"{self.starttime} {self.endtime}"