from django import forms
from .models import Student #current directory

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"