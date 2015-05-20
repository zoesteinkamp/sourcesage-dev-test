__author__ = 'zoesteinkamp'
from swampdragon.serializers.model_serializer import ModelSerializer

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = 'start.Answer'
        publish_fields = ('answerer','post', 'answer')
        update_fields = ('answerer','post', 'answer')

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = 'start.Question'
        publish_fields = ('poster', 'title', 'content')
        update_fields = ('poster', 'title', 'content')