from django.urls import path

from . import views

app_name='surveys'

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add_survey"),
    path('<int:survey_id>/', views.detail, name='detail'),
    path('<int:survey_id>/delete', views.delete, name='delete'),
    #path('<int:survey_id>/edit', views.update, name='edit')
]