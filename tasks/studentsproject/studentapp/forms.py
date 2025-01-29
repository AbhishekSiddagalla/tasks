from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from studentapp.models import Exam

class ExamForm(forms.ModelForm):

        model = Exam
        fields = "__all__"