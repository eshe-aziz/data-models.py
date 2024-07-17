from django.urls import path
from .views import StudentListView, ClassPeriodListView, TeacherListView, CourseListView, ClassroomListView


urlpatterns = [
    path("student/", StudentListView.as_view(), name = "student_list_view"),
    path("classperiod/", ClassPeriodListView.as_view(), name = "classperiod_list_view"),
    path("teacher/", TeacherListView.as_view(), name = "teacher_list_view"),
    path("course/", CourseListView.as_view(), name = "course_list_view"),
    path("classroom/", ClassroomListView.as_view(), name = "classroom_list_view")
]
