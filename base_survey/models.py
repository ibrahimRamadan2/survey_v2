from django.db import models


class BaseSurvey(models.Model):
    name = models.CharField(max_length=50 , required=True , null=False , blank=False) 
    paused = models.BooleanField(default=False)
    end_at = models.DateTimeField(required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.DateTimeField(default=False) 

class QuestionType(models.Model):
    type = models.CharField(max_length=50 , required = True, null= False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    content = models.JSONField(required= True,  null=False)
    question_type = models.ForeignKey(QuestionType , on_delete=models.CASCADE )
    order = models.IntegerField(blank=False , null = False)
    required = models.BooleanField(default=False)


class Choise(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    content = models.TextField(required = True , blank = False , null = False )




