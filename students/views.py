from django.shortcuts import render, get_object_or_404
from .models import Student

def studentlist(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request,id):
    student=get_object_or_404(Student,id=id)
    return render(request,'student_detail.html',{'student':student})

