from django.urls import path
from .views import StudentListView

urlpatterns = [
    path("student/", StudentListView.as_view(), name = "student_list_view"),
]
