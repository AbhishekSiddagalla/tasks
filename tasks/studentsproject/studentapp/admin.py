from django.contrib import admin
from studentapp.models import (ClassRoom,Subject,ClassWiseStudent,
                               ClassRoomWiseSubjectWithTeacher,
                               Exam,ExamType,FailedStudent,Teacher,
                               StudentWithHobbies,Hobbies)

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['classroom']
admin.site.register(ClassRoom)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['std_id','std_name','study_in']

admin.site.register(Subject)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['student','class_room']
admin.site.register(ClassWiseStudent)

class TeacherNameAdmin(admin.ModelAdmin):
    list_display = ['teacher_name']
admin.site.register(Teacher)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['class_room','teacher_name','student_name']
admin.site.register(ClassRoomWiseSubjectWithTeacher)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['exam_type','class_room','student','teacher',
                    'sub1','sub2','sub3','sub4','sub5','sub6','total','hobby']
admin.site.register(Exam)

class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ['exam_type']
admin.site.register(ExamType)

class FailedStudentsAdmin(admin.ModelAdmin):
    list_display = ['student','class_room','exam','status']
admin.site.register(FailedStudent)

class Admin(admin.ModelAdmin):
    list_display = ['hobby']
admin.site.register(Hobbies)

class StudentsWithHobbiesAdmin(admin.ModelAdmin):
    list_display = ['student','hobby','total']
admin.site.register(StudentWithHobbies)