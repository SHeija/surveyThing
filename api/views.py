from rest_framework import generics
from . import serializers
from rest_framework import serializers as ser_tools
from surveys import models


# REST views
# XDetail = view for get, put, delete
# XCreate = view for post

class SurveyList(generics.ListAPIView):
    queryset = models.Survey.objects.all()
    serializer_class = serializers.SurveySerializer

class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Survey.objects.all()
    serializer_class = serializers.SurveySerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer

class QuestionAdd(generics.CreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionCreateSerializer

class SurveyAdd(generics.CreateAPIView):
    queryset = models.Survey.objects.all()
    serializer_class = serializers.SurveyCreateSerializer

    #author cannot be set manually
    author = ser_tools.HiddenField(default=ser_tools.CurrentUserDefault())
    
    #saves current user as an author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer

class AnswerAdd(generics.CreateAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
