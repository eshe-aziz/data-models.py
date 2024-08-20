from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from .serializers import MinimalStudentSerializer
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
        # serializer = StudentSerializer(students, many = True)
        serializer = MinimalStudentSerializer(students, many = True)
        
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

    
    def unenroll_student(self, student, course_id):
        course = Course.objects.get(id = course_id)
        student.course.add(course)


    def add_to_class(self, student, class_id):
        classroom = Classroom.objects.get(id = class_id)
        classroom.student.add(student)


    def post(self, request, id):
        student = Student.objects.get(id = id)
        action = request.data.get("action")

        if action == "enroll":
            course_id = request.data.get("course")
            self.enroll_student(student, course_id)

            return Response(status.HTTP_201_CREATED)
    

        # elif action == "unenroll_student":
        # course_id = request.data.get("course_id")
        # self.unenroll_student(student, course_id)
        # return Response(status = status.HTTP_200_OK)
    
        # elif action == "add_to_class":
        #     class_id = request.data.get("class_id")
        #     self.add_to_class(student, class_id)
        #     return Response(status = status.HTTP_201_CREATED)
    
        # else:
        # return Response(status= status.HTTP_400_BAD_REQUEST)

        elif action == "unenroll_student":
            course_id = request.data.get("course_id")
            self.unenroll_student(student, course_id)
            return Response(status=status.HTTP_200_OK)

        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
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
    
    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_classperiod":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_classperiod(teacher_id, course_id)
            return Response(status = status.HTTP_201_CREATED)
        
        elif action == "get_timetable":
            self.get_timetable(id)
            return Response(status = status.HTTP_201_CREATED)
        
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
    def create_classperiod(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id = teacher_id)
        course = Course.objects.get(id = course_id)
        classperiod = ClassPeriod(teacher = teacher, course = course)
        classperiod.save()
        return Response(status = status.HTTP_201_CREATED)
    
    def get_timetable(self, request, id):
        classperiod = ClassPeriod.objects.get(id = id)
        timetable = []
        for day in range(7):
            day_timetable = []
            for period in classperiod.periods.filter(day = day):
                day_timetable.append({
                    'start_time': period.start_time,
                    'end_time': period.end_time,
                    'course': period.course.name,
                    'student_class': period.classroom
                })

        timetable.append(day_timetable)
        return Response({'timetable': timetable})
    

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
    
    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id = course_id)
        teacher.course.add(course)

    def assign_class(self, teacher, class_id):
        classroom = Classroom.objects.get(id = class_id)
        classroom.teacher = teacher
        classroom.save()

    
    def post(self, request, id):
        teacher = Teacher.objects.get(id = id)
        action = request.data.get("action")

        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status = status.HTTP_201_CREATED)
        
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status = status.HTTP_201_CREATED)
        
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
#########################################################################################################
class CourseListView(APIView):
    def get(self, request): 
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        
        return Response(serializer.data)
    
    def put(self, request): #it was post before
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
        classroom = Classroom.objects.get(id = id)
        serializer = ClassroomSerializer(classroom, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id):
        classroom = Classroom.objects.get(id = id)
        classroom.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    


