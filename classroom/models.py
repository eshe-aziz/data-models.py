from django.db import models

# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    level = models.CharField(max_length= 50)
    duration = models.DurationField()
    capacity = models.PositiveIntegerField()
    materials = models.TextField()
    schedule = models.DateTimeField()
    location = models.CharField(max_length= 50)
    resources = models.TextField()
    students = models.PositiveSmallIntegerField()


    def __str__(self):
        return f"{self.name} {self.description}"







