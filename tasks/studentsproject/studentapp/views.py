import itertools
from faker import Faker
import random
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import (Exam, ExamType, ClassRoom,Subject,FailedStudent,
                     Teacher,Hobbies)
from .forms import ExamForm
from model_bakery import baker
from django.http import JsonResponse
from django.db.models import Q


def student_exam_report(request):

    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        form = ExamForm()
        return render(request,"formsapp/exam_report.html",{'form':form})
    form = ExamForm()
    return render(request, "formsapp/exam_report.html", {'form': form})

def populate(request):
    class_rooms = ("class1", "class2", "class3", "class4", "class5", "class6", "class7", "class8", "class9", "class10")
    exam_types = ("unittest1", "unittest2", "unittest3", "quarterly", "halfyearly", "annually")
    subjects = ("Telugu","Hindi","English","Maths","Science","Social")
    teacher_names = ["Jenny","Robert","Lucy","Ben","Parker","John","Charlie","Bobby","Ruby","Sam"]
    hobbies = ["Cricket","Football","Basketball","Kabbadi","kho-Kho","volleyball","Baseball","Powerlifting","Running","Carroms","Chess"]

    exam_type_instances = [baker.make(ExamType, exam_type = examType, make_m2m=True) for examType in exam_types]
    class_room_instances = [baker.make(ClassRoom, name=class_room, make_m2m=True) for class_room in class_rooms]
    subject_instances = [baker.make(Subject,subject_name=subject, make_m2m=True) for subject in subjects ]
    teacher_name_instances = [baker.make(Teacher,teacher_name=teacher_name, make_m2m=True) for teacher_name in teacher_names]
    hobby_instances = [baker.make(Hobbies,hobby=hobbies,make_m2m=True) for hobbies in hobbies]
    fake = Faker()

    users = []
    for _ in range(500):
        user = baker.make(User, make_m2m=True)
        while True:
            user_name = fake.first_name()
            if len(user_name) < 10:
                break
        user.first_name = user_name
        user.save()
        users.append(user)

    exam_type_cycle = itertools.cycle(exam_type_instances)
    class_room_cycle = itertools.cycle(class_room_instances)
    subject_cycle = itertools.cycle(subject_instances)
    teacher_name_cycle = itertools.cycle(teacher_name_instances)
    # hobby_cycle = itertools.cycle(hobby_instances)

    exam_instances = []
    for i in range(500):
        user = random.choice(users)
        selected_hobbies = random.sample(hobby_instances,3)
        exam = baker.make(
            Exam,
            sub1=random.randint(0, 100),
            sub2=random.randint(0, 100),
            sub3=random.randint(0, 100),
            sub4=random.randint(0, 100),
            sub5=random.randint(0, 100),
            sub6=random.randint(0, 100),
            hobby=selected_hobbies,
            exam_type=next(exam_type_cycle),
            class_room=next(class_room_cycle),
            student=user,
            teacher=next(teacher_name_cycle)
        )
        exam_instances.append(exam)

    exam_data = []
    for exam in exam_instances:
        exam_data.append({
            "exam_type": exam.exam_type.exam_type,
            "class_room": exam.class_room.name,
            "student": exam.student.username,
            "teacher": exam.teacher.teacher_name,
            "sub1": exam.sub1,
            "sub2": exam.sub2,
            "sub3": exam.sub3,
            "sub4": exam.sub4,
            "sub5": exam.sub5,
            "sub6": exam.sub6,
            "hobby" : [hobby.hobby for hobby in exam.hobby.all()]
        })
    return JsonResponse({"exams": exam_data})

def check_failed_students(self):
    ex = Exam.objects.filter(Q(sub1__lt=35) |Q(sub2__lt=35)|Q(sub3__lt=35)|
                             Q(sub4__lt=35)|Q(sub5__lt=35)|Q(sub6__lt=35))
    ex=ex.filter(exam_type__exam_type="halfyearly",class_room__name="class7")

    print(ex.count())
    class7={"count":ex.count()}
    return JsonResponse(class7)

def teacherwise_failed_students(self):
    failed_students_list = Exam.objects.filter(
                                              Q(sub1__lt=35) |Q(sub2__lt=35)|Q(sub3__lt=35)|
                                              Q(sub4__lt=35)|Q(sub5__lt=35)|Q(sub6__lt=35),
                                              )
    failed_students_list=failed_students_list.filter(teacher__teacher_name="Lucy",exam_type__exam_type="halfyearly")
    failedstudents={"failed_students_count":failed_students_list.count()}
    return JsonResponse(failedstudents)

def student_hobby(self):
    student_hobby_list = Exam.objects.prefetch_related('hobby')

    student_hobbies = student_hobby_list.filter(Q(sub1__gt=60) | Q(sub2__gt=60) | Q(sub3__gt=60) |
        Q(sub4__gt=60) | Q(sub5__gt=60) | Q(sub6__gt=60) ,exam_type__exam_type="halfyearly")
    student_hobby_list = student_hobby_list.values('student__username','total','hobby__hobby')
    print(student_hobby_list)

    studenthobbies = {"student count":student_hobbies.count(),
                      "student_hobbies":list(student_hobby_list)}
    return JsonResponse(studenthobbies)

