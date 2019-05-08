from rest_framework import serializers
from surveys import models

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    #taikaluokka, jonka perimällä serializereille voi initissä määritellä mitä kenttiä käytetään
    #en päätynyt käyttämään, mutta jos haluaa jatkaa ja tehdä monimutkaisempia rajapintoja, niin hyödyllinen

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class AnswerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        fields = ('id', 'question', 'answer_text')
        model = models.Answer

class QuestionSerializer(DynamicFieldsModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        fields = ('id', 'survey', 'question_text', 'answers')
        model = models.Question

class QuestionCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        fields = ('id', 'survey', 'question_text')
        model = models.Question

class SurveySerializer(DynamicFieldsModelSerializer):
    questions = QuestionSerializer(many=True, read_only=False,)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        fields = ('id', 'title','description','author','date_created', 'questions')
        model = models.Survey

class SurveyCreateSerializer(DynamicFieldsModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        fields = ('id', 'title','description','author','date_created')
        model = models.Survey


