from django.contrib import admin
from studentapp.models import ClassRoom,Subject,ClassWiseStudent,ClassRoomWiseSubjectWithTeacher,Exam,ExamType,FailedStudent

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['classroom']
admin.site.register(ClassRoom)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['std_id','std_name','study_in']

admin.site.register(Subject)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['student','class_room']
admin.site.register(ClassWiseStudent)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']
admin.site.register(ClassRoomWiseSubjectWithTeacher)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['exam_type','class_room','student','sub1','sub2','sub3','sub4','sub5','sub6','total']
admin.site.register(Exam)

class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ['exam_type']
admin.site.register(ExamType)

class FailedStudentsAdmin(admin.ModelAdmin):
    list_display = ['student','class_room','exam','status']
admin.site.register(FailedStudent)