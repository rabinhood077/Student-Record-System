from student_app import views
from django.urls import path
from student_app import views


urlpatterns = [
  path('', views.student_list, name='student-list'),
  path('student_detail/<int:pk>/', views.student_detail, name='student-detail'),
  path('delete-student/<int:pk>/', views.delete_student, name='delete-student'),
 
  path('update-student/<int:pk>/', views.update_student, name='update-student'),
  path('add-student/', views.add_student, name='add-student'),
  
    
    
]
