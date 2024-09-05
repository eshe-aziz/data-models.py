# from django.shortcuts import render, redirect
# from .forms import StudentRegistrationForm

# # Create your views here.
# def register_student(request): #request- represents the HTTP request
#     if request.method == "POST":
#         form = StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect("register_student")

#         else:
#             form = StudentRegistrationForm()

#         return render(request, "student/register_student.html", {"form": form})



from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

# Create your views here.
def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_student")  # This needs to be followed by `return` to stop further execution

    else:
        form = StudentRegistrationForm()

    return render(request, "student/register_student.html", {"form": form})
