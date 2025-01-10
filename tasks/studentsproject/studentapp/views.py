import itertools
from faker import Faker
import random
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Exam, ExamType, ClassRoom,Subject,FailedStudent
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

    exam_type_instances = [baker.make(ExamType, exam_type = examType, make_m2m=True) for examType in exam_types]
    class_room_instances = [baker.make(ClassRoom, name=class_room, make_m2m=True) for class_room in class_rooms]
    subject_instances = [baker.make(Subject,subject_name=subject) for subject in subjects ]

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

    exam_instances = []
    for i in range(500):
        # Randomly select a user from the users list
        user = random.choice(users)

        exam = baker.make(
            Exam,
            sub1=random.randint(0, 100),
            sub2=random.randint(0, 100),
            sub3=random.randint(0, 100),
            sub4=random.randint(0, 100),
            sub5=random.randint(0, 100),
            sub6=random.randint(0, 100),
            exam_type=next(exam_type_cycle),  # Get the next exam_type from the cycle
            class_room=next(class_room_cycle),  # Get the next class_room from the cycle
            student=user  # Link user to exam instance
        )
        exam_instances.append(exam)

    # Prepare data to return in JSON format
    exam_data = []
    for exam in exam_instances:
        exam_data.append({
            "exam_type": exam.exam_type.exam_type,  # Access the ForeignKey field directly
            "class_room": exam.class_room.name,  # Access the ForeignKey field directly
            "student": exam.student.username,  # Access the User's username
            "sub1": exam.sub1,
            "sub2": exam.sub2,
            "sub3": exam.sub3,
            "sub4": exam.sub4,
            "sub5": exam.sub5,
            "sub6": exam.sub6
        })

    # Return the exam data as a JSON response
    return JsonResponse({"exams": exam_data}, safe=False)

def check_failed_students(self):
    ex = Exam.objects.filter(Q(sub1__lt=35) |Q(sub2__lt=35)|Q(sub3__lt=35)|
                             Q(sub4__lt=35)|Q(sub5__lt=35)|Q(sub6__lt=35))
    ex=ex.filter(exam_type__exam_type="halfyearly",class_room__name="class7")

    print(ex.count())
    class7={"count":ex.count()}
    return JsonResponse(class7)

