from django.db import models
from datetime import datetime
from django.utils import timezone 


class BaseSurvey(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)
    paused = models.BooleanField(default=False)
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=datetime(2022, 1, 1, 0, 0).strftime("%Y-%m-%d %H:%M:%S"))
    is_published = models.BooleanField(default=False)  
    is_deleted = models.BooleanField(default=False) 
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def copy_survey(self , survey):
        self.name = survey.name 
        self.paused = survey.paused 
        self.end_at = survey.end_at 
        self.published_at = survey.published_at 
        self.is_published = survey.is_published 
        self.is_deleted = survey.is_deleted
        self.save()

class Question(models.Model):
    content = models.JSONField( null=False , blank=False)
    survey= models.ForeignKey(BaseSurvey,related_name="questions",on_delete=models.CASCADE)
    question_type = models.CharField(max_length=10 , null=False , blank=False)
    order = models.IntegerField(blank=False , null = False)
    required = models.BooleanField(default=False)
    def __repr__(self) -> str:
        return f"{self.content}"



class Choise(models.Model):
    question = models.ForeignKey(Question ,related_name="choices" ,on_delete=models.CASCADE)
    content = models.TextField( blank = False , null = False )








