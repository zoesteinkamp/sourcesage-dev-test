from django import forms
from django.forms import ModelForm
from models import Question, Answer

__author__ = 'zoesteinkamp'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['poster', 'title', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answerer','post']
        exclude = ['answer']