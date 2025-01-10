from django.urls import path
from studentapp import views  # Import views from your current directory

urlpatterns = [
    path('populate/', views.populate, name='populate'),
    path('class6/', views.check_failed_students,name='class6')
]
