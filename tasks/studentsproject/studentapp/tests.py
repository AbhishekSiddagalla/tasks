

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.http import JsonResponse
from .models import Exam, ClassRoom, ExamType



class CheckFailedStudentsTestcase(TestCase):
    def test_student_info(self):
        self.exam_type_halfyearly = ExamType.objects.create(exam_type="halfyearly")
        self.class_6 = ClassRoom.objects.create(name="class6")
        self.student_1 = Exam.objects.create(
                                            exam_type=self.exam_type_halfyearly,
                                             name=self.class_6,
                                             sub1=34,sub2=45,sub3=76,
                                             sub4=65,sub5=23,sub6=55
                                             )
        self.student_2 = Exam.objects.create(
                                            exam_type=self.exam_type_halfyearly,
                                            name=self.class_6,
                                            sub1=33, sub2=15, sub3=66,
                                            sub4=85, sub5=33, sub6=45
                                            )
        self.student_3 = Exam.objects.create(
                                            exam_type=self.exam_type_halfyearly,
                                            name=self.class_6,
                                            sub1=4, sub2=35, sub3=77,
                                            sub4=99, sub5=69, sub6=44
                                            )
        self.student_4 = Exam.objects.create(
                                            exam_type=self.exam_type_halfyearly,
                                            name=self.class_6,
                                            sub1=35, sub2=85, sub3=76,
                                            sub4=43, sub5=73, sub6=89
                                            )

    def test_failed_students_class6(self):
        c =Client()
        response = c.get(reverse('class/'))
        self.assertEqual(response.status_code,200)
        data = response.json()
        self.assertEqual((data['count'],3))
