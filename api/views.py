from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from course.models import Course
from .serializers import CourseSerializer
from classroom.models import Classroom
from .serializers import ClassroomSerializer



# QUERING DATA- GET
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")
        if first_name:
            students = students.filter(first_name = first_name)

        if country:
            students = students.filter(country = country)
        serializer = StudentSerializer(students, many = True)
        
        return Response(serializer.data)
    

# SAVING DATA- POST
    def post(self, request):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

# Dealing with a single object 
class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    

    def put(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    

    def enroll_student(self, student, course_id):
        course = Course.objects.get(id = course_id)
        student.course.add(course)


    def post(self, request, id):
        student = Student.objects.get(id = id)
        action = request.data.get("action")
        if action: "enroll"
        course_id = request.data.get("course")
        self.enroll_student(student, course_id)

        return Response(status.HTTP_201_CREATED)

    
# ############################################################################################################

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many = True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    

    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(classperiod, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id):
        classperiod = ClassPeriod.objects.get(id = id)
        classperiod.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    

 #################################################################################################### 

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many = True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    

    def put(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    
#########################################################################################################
class CourseListView(APIView):
    def get(self, request): 
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, id):
        student = Student.objects.get(id = id)
        action = request.data.get("action")
        if action: "enroll"
        course_id = request.data.get("course")
        self.enroll_student(student, course_id)

        return Response(status.HTTP_201_CREATED)
    
class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    

    def put(self, request, id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id):
        course = Course.objects.get(id = id)
        course.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    

##################################################################################################################

class ClassroomListView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many = True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassroomSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom = Classroom.objects.get(id = id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    

    def put(self, request, id):
        course = Classroom.objects.get(id = id)
        serializer = ClassroomSerializer(Classroom, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id):
        classroom = Classroom.objects.get(id = id)
        classroom.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    
    
    def add_student(self, classroom, student_id):
        student = Student.objects.get(id = student_id)
        student.add_(student)


    def post(self, request, id):
        student = Student.objects.get(id = id)
        action = request.data.get("action")
        if action: "enroll"
        classroom_id = request.data.get("classroom")
        self.add_student(student, classroom_id)

        return Response(status.HTTP_201_CREATED)
    


