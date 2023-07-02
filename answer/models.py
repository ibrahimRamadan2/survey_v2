from django.db import models
from base_survey.models import Choise ,Question,BaseSurvey 
# Create your models here.
class Answer(models.Model):
    choice = models.ForeignKey(Choise , required=True ,  on_delete=models.CASCADE)
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    content = models.TextField(default= "" )
    created_at = models.DateTimeField(auto_now_add=True)

class Respondant(models.Model):
    survey = models.ForeignKey(BaseSurvey , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


