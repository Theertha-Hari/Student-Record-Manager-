from django.shortcuts import render, get_object_or_404
from .models import Student
from .forms import StudentForm

def studentlist(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request,id):
    student=get_object_or_404(Student,id=id)
    return render(request,'student_detail.html',{'student':student})

def student_update(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
    else:
        form=StudentForm(instance=student)
    return render(request,'student_update.html',{'form':form,'student':student})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()  
    else:
        form = StudentForm()

    return render(request, 'student_add.html', {'form': form})