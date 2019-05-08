from django.urls import path

from . import views

#name for cross-linking from other apps
app_name='surveys'

urlpatterns = [
    path('add/', views.add, name="add_survey"),
    path('<int:survey_id>/', views.detail, name='detail'),
    path('<int:survey_id>/delete', views.delete, name='delete'),
    path('<int:survey_id>/edit_survey', views.edit_survey, name='edit_survey'),
    #path('<int:survey_id>/edit_questions', views.edit_questions, name='edit_questions') #broken
]