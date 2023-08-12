from django.db import models
from base_survey.models import Choise ,Question,BaseSurvey 
# Create your models here.
class Respondant(models.Model):
    survey = models.ForeignKey(BaseSurvey , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    choice = models.ForeignKey(Choise ,  on_delete=models.CASCADE)
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    content = models.TextField(default= "")
    respondant = models.ForeignKey(Respondant, related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

"""
    submiting survey should return data like that (group of answers):



"""