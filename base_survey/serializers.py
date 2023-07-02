from rest_framework import serializers 
from base_survey.models import BaseSurvey , Question ,QuestionType , Choise
import datetime
class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseSurvey
        fields = '__all__' 
                

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__' 

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__' 

class ChoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choise
        fields = '__all__' 