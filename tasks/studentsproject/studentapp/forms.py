from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from studentapp.models import Exam

class ExamForm(forms.ModelForm):
    # exam_type = forms.CharField(max_length=20)
    # class_room = forms.CharField(max_length=10)
    # student = forms.CharField(max_length=20)
    # sub1 = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
    #                           label='Enter a number between 1 and 100')
    # sub2 = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
    #                           label='Enter a number between 1 and 100')
    # sub3 = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
    #                           label='Enter a number between 1 and 100')
    # sub4 = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
    #                           label='Enter a number between 1 and 100')
    # sub5 = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
    #                           label='Enter a number between 1 and 100')
    # sub6 = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
    #                           label='Enter a number between 1 and 100')
    class Meta:
        model = Exam
        fields = "__all__"