from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    qualification = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 25)
    title = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 10)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"