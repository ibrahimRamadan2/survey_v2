from rest_framework import serializers
from .models import Answer,Respondant
from base_survey.models import BaseSurvey,Question, Choise

class AnswerSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    survey_id = serializers.IntegerField()
    content = serializers.CharField()
    def create(self, validated_data):
        survey = BaseSurvey.objects.get(id=validated_data["survey_id"])
        respondant = Respondant.objects.create(survey=survey)
        question = Question.objects.get(id= validated_data["question_id"])
        choice = Choise.objects.get(id=validated_data["choice_id"])
        content=  validated_data['content']
        answer = Answer.objects.create(respondant=respondant , question=question ,choice=choice, content=content)
        return answer
    class Meta:
        model = Answer
        fields =['choice_id',"question_id","respondant_id", "content"]

    









