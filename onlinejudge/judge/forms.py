from django import forms
from .models import Problem, Testcases, Submissions
from django.contrib.auth.models import User


class ProblemForm(forms.ModelForm):
    problem_name = forms.CharField()
    problem_desc = forms.CharField(widget=forms.Textarea)
    diff = forms.CharField()

    class Meta:
        model = Problem
        fields = ['problem_name', 'problem_desc', 'diff']


class SubmissionForm(forms.ModelForm):
    langs = [("C", "C"),  ("CPP", "C++"), ("JAVA", "Java"), ("PYTH", "python"), ("PYTH3", "python 3")]
    code = forms.CharField(widget=forms.FileInput)
    lang = forms.ChoiceField(choices=langs)
    file = forms.FileField()

    class Meta:
        model = Submissions
        fields = ['code', 'lang', 'file']