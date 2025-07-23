from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from student_app.models import Student
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from student_app.forms import StudentForm



# from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class StudentList(ListView):
  model=Student
  template_name="student_list.html"
  context_object_name="students"

  def get_queryset(self):
     queryset=Student.objects.all()
     return queryset
  



class StudentDetail(DetailView):
   model=Student
   template_name="student_detail.html"
   context_object_name="student"

   def get_queryset(self):
      queryset=Student.objects.filter(pk=self.kwargs["pk"])
      return queryset
       

class Update_Student(UpdateView):
   model=Student
   template_name="Add_student.html"
   form_class=StudentForm

   def get_success_url(self):
      student=self.get_object()
      return reverse_lazy('student-list')

   

class Delete_Student(View):
   def get(self,request,pk):
      student=Student.objects.get(pk=pk)
      student.delete()
      return redirect('student-list')
      



class AddStudent(CreateView):
  model=Student
  template_name="add_student.html"
  form_class=StudentForm


  def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

  def get_success_url(self):
        return '/'

  


  
  

  
  
