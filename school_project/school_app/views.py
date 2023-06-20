from django.shortcuts import render, redirect
from .models import Department, Course, Purpose, Material, Student
from .forms import StudentForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()

    context = {
        'form': form,

    }
    return render(request, 'create_student.html', context)


def success(request):
    return render(request, 'success.html')
