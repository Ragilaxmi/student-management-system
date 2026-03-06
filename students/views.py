from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm


def student_list(request):

    students = Student.objects.all()

    return render(request,'student_list.html',{'students':students})


def add_student(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'add_student.html',{'form':form})


def delete_student(request,id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')