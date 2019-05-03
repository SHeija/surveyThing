from django.db import models

class Survey (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField()
    def __str__(self):
        return self.title

class Question (models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, verbose_name='Question')
    def __str__(self):
            return self.question_text

class Answer (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
            return self.answer_text
