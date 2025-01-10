from importlib.metadata import requires

from django.contrib.auth.models import User
from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        if not self.name:
            return "NA"
        return self.name

class Subject(models.Model):
    subject_name = models.CharField(max_length=15)

    def __str__(self):
        return self.subject_name

class ClassWiseStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.class_room} - {self.student}"

class ClassRoomWiseSubjectWithTeacher(models.Model):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.class_room} - {self.subject} - {self.teacher}"

class ExamType(models.Model):
    exam_type = models.CharField(max_length=20)

    def __str__(self):
        return self.exam_type

class Exam(models.Model):

    exam_type = models.ForeignKey(ExamType, on_delete=models.SET_NULL, null=True)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    sub1 = models.PositiveIntegerField(verbose_name="telugu")
    sub2 = models.PositiveIntegerField(verbose_name="hindi")
    sub3 = models.PositiveIntegerField(verbose_name="english")
    sub4 = models.PositiveIntegerField(verbose_name="maths")
    sub5 = models.PositiveIntegerField(verbose_name="Science")
    sub6 = models.PositiveIntegerField(verbose_name="social")
    total = models.PositiveIntegerField(null = True,default=None, blank=True)


    def total_marks(self):
        student = Exam.objects.all()
        total_marks = (self.sub1 + self.sub2 + self.sub3
                       + self.sub4 + self.sub5 + self.sub6)
        return total_marks

    def save(self):
        self.total = self.total_marks()
        super().save()

    def __str__(self):
        return f"{self.exam_type} - {self.class_room} - {self.student} "


class FailedStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    exam_type = models.ForeignKey(ExamType, on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=10,default=None,null=True,blank=True)


    # def check_failed_students(self):
    #     # class_6 = ClassRoom.objects.filter(name="class6").first()
    #
    #     exams = Exam.objects.filter(class_room="class6")
    #     for exam in exams:
    #         if (exam.sub1 < 35 or exam.sub2 < 35 or exam.sub3 < 35 or
    #                 exam.sub4 < 35 or exam.sub5 < 35 or exam.sub6 < 35):
    #             failed_student, created = FailedStudent.objects.get_or_create(
    #                 student=exam.student,
    #                 class_room=exam.class_room,
    #                 exam_type=exam.exam_type,
    #                 defaults={'status': 'failed'}
    #             )
    #             if not created:
    #                 failed_student.status = 'failed'
    #                 failed_student.save()
    #     return []

    def __str__(self):
        return f" {self.student} - {self.class_room} - {self.exam_type}"











