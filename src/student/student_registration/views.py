from django.shortcuts import render, redirect        # render and redirect are called this below functions
from .forms import StudentForm
from django.contrib import messages
from .models import Student

def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request,'student_registration/student_list.html', context)

def student_form(request, id=0):
    # "If condition" is made here to deal with both GET and POST on this function.
    if request.method == "GET":
        if id == 0:
            form =  StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request,'student_registration/student_form.html', {'form': form})
    else:
        if id == 0:
            form =  StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance= student)
        if form.is_valid():
            form.save()
            # messages.success(request, f' The Student is successfully registered!')
        return redirect('/student/list')
        
def student_delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')