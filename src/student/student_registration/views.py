from django.shortcuts import render, redirect        # render and redirect are called this below functions
from .forms import StudentForm
from django.contrib import messages
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout



@login_required(login_url='/login/')
def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request,'student_registration/student_list.html', context)

@login_required(login_url='/login/')
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

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f"You are now logged in as {username}")
            return redirect('student/')
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "student_registration/login.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("logout")