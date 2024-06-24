from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    gender = models.CharField(max_length= 20)
    email = models.EmailField()
    country = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    course = models.CharField(max_length= 50)
    bio = models.CharField(max_length = 200)
    guardian_name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

















