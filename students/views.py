from django.shortcuts import render
from .models import Student

def studentlist(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

