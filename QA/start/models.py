from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import AnswerSerializer, QuestionSerializer

__author__ = 'zoesteinkamp'

# A simple question class that the poster will use to fill out a model form
class Question(SelfPublishModel, models.Model):
    serializer_class = QuestionSerializer
    id = models.AutoField(primary_key=True)
    poster = models.CharField(unique=True, max_length=40)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=300)


    def __unicode__(self):
        return self.title

# the Answer class the is a foreign key to the question model
class Answer(SelfPublishModel, models.Model):
    serializer_class = AnswerSerializer
    id = models.AutoField(primary_key=True)
    answerer = models.CharField(unique=True, max_length=40)
    post = models.TextField(max_length=3000)
    answer = models.ForeignKey('Question')

    def __unicode__(self):
        return self.answerer

