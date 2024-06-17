from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length= 50)
    course_location = models.CharField(max_length= 20)
    course_department = models.CharField(max_length= 50)
    course_description = models.CharField(max_length= 100)
    course_level = models.CharField(max_length= 20)
    course_capacity = models.PositiveBigIntegerField()
    course_duration = models.DurationField()
    course_trainer = models.PositiveSmallIntegerField()
    course_code = models.PositiveSmallIntegerField()
    course_price = models.DecimalField(max_digits= 8, decimal_places= 2, default= '1000000.00')

    def __str__(self):
        return f"{self.course_name} {self.course_price}"