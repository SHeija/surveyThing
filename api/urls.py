from django.urls import path
from . import views

urlpatterns = [
    path('surveys/', views.SurveyList.as_view()),
    path('surveys/<int:pk>/', views.SurveyDetail.as_view()),
    path('surveys/add/', views.SurveyAdd.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('questions/add/', views.QuestionAdd.as_view()),
    path('answers/<int:pk>/', views.AnswerDetail.as_view()),
    path('answers/add/', views.AnswerAdd.as_view())
]