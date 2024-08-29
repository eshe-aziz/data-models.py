from django.db import models
from course.models import Course

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    gender = models.CharField(max_length= 20)
    email = models.EmailField()
    country = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    course = models.ManyToManyField(Course)
    bio = models.CharField(max_length = 50, default='default_bio_value')
    guardian_name = models.CharField(max_length = 50, default='default_guardian_name_value')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

















