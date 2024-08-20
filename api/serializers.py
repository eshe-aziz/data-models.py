from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'

class CourseSerializer(serializers.ModelSerializer): #should be above studentserializer
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many = True)
    class Meta:
        model = Student
        fields = '__all__'

class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["first_name", "email"]

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"
    
    class Meta:
        model = Student
        fields = ["id", "full_name", "email"]

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['starttime', 'endtime']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']


# class CourseSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = Course
#         fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        

class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'capacity']






