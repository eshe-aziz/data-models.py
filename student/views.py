from django.shortcuts import render
from .forms import StudentRegistrationForm

# Create your views here.
def register_student(request): #request- represents the HTTP request
    form = StudentRegistrationForm()

    return render(request, "student/register_student.html", #name of the template we are going to create to be able to render
    {"form": form})