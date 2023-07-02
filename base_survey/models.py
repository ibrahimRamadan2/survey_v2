from django.db import models
import  datetime 
from django.utils import timezone 


class BaseSurvey(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False) 
    paused = models.BooleanField(default=False)
    end_at = models.DateTimeField(null = False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False) 
    
    def __repr__(self) -> str:
        return f"{self.name}"
    

class QuestionType(models.Model):
    type = models.CharField(max_length=50 , null= False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self) -> str:
        return f"{self.type}"

class Question(models.Model):
    content = models.JSONField( null=False , blank=False)
    question_type = models.ForeignKey(QuestionType , on_delete=models.CASCADE )
    order = models.IntegerField(blank=False , null = False)
    required = models.BooleanField(default=False)
    def __repr__(self) -> str:
        return f"{self.content}"

class Choise(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    content = models.TextField( blank = False , null = False )




