from django.urls import path
from . import views #imports the entire file

urlpatterns = [
    path("register/", views.register_student, name= "register_student"),
]