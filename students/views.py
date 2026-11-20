from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


# CREATE
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/create.html', {'form': form})


# READ + SEARCH
def student_list(request):
    search = request.GET.get('search', '')

    if search:
        student_list = Student.objects.filter(name__icontains=search)
    else:
        student_list = Student.objects.all()

    return render(
        request,
        'students/list.html',
        {'student_list': student_list, 'search': search}
    )


# UPDATE
def student_update(request, id):
    student = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/update.html', {'form': form})


# DELETE
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/delete.html', {'student': student})

# Create your views here.
