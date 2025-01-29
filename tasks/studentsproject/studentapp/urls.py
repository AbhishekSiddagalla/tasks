from django.urls import path
from studentapp import views  # Import views from your current directory

urlpatterns = [
    path('populate/', views.populate, name='populate'),
    path('class/', views.check_failed_students,name='class_wise_failed_students'),
    path('failedstudents/',views.teacherwise_failed_students,name='teacher_wise_failed_students'),
    path('hobbies/',views.student_hobby,name='Student_hobbies')
]
