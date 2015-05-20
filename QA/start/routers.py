from .serializers import AnswerSerializer, QuestionSerializer
from .models import Answer, Question
from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter


class AnswerRouter(ModelRouter):
    serializer_class = AnswerSerializer
    model = Answer
    route_name = 'answer'

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

class QuestionRouter(ModelRouter):
    serializer_class = QuestionSerializer
    model = Question
    route_name = 'question'

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

route_handler.register(AnswerRouter)
route_handler.register(QuestionRouter)