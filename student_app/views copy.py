from django.shortcuts import render
from student_app.models import Student
from django.http import HttpResponseRedirect
# Create your views here.


def student_list(request):
  students=Student.objects.all()

  return render(
    request,
    "student_list.html",
    {'students':students},
  )



def student_detail(request,pk):
  student=Student.objects.get(pk=pk)
  return render(
    request,
    "student_detail.html",
    {'student':student}
  )



def update_student(request,pk):
  if request.method=='GET':
    student=Student.objects.get(pk=pk)
    return render(
      request,
      'update_student.html',
      {'student':student},
    )
  
  else:
    student=Student.objects.get(pk=pk)
    student.name=request.POST['name']
    student.age=request.POST['age']
    student.email=request.POST['email']
    student.save()
    return HttpResponseRedirect("/")
  


def delete_student(request,pk):
  student=Student.objects.get(pk=pk)
  student.delete()
  return HttpResponseRedirect("/")





def add_student(request):
    if request.method == 'GET':
        return render(request, "add_student.html")
    else:
        # Create a single student with all fields
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email'],
            image=request.FILES.get('image')  # Using get() to handle case when no image is uploaded
        )
        return HttpResponseRedirect("/")
  
  
  

  
  
