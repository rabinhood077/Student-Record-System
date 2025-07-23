from student_app import views
from django.urls import path
from student_app import views


urlpatterns = [
  path('', views.StudentList.as_view(), name='student-list'),
  path('student_detail/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
  path('delete-student/<int:pk>/', views.Delete_Student.as_view(), name='delete-student'),
 
  path('update-student/<int:pk>/', views.Update_Student.as_view(), name='update-student'),
  path('add-student/', views.AddStudent.as_view(), name='add-student'),
  
    
    
]
