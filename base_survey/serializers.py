from rest_framework import serializers 
from base_survey.models import BaseSurvey , Question ,QuestionType , Choise
import datetime
           
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__' 
    
    def create(self,validated_data):
        type = validated_data.pop("type")
        type = QuestionType.get_type(type)
        question = Question.create(type=type , **validated_data)
        return question

    def update(self, instance, validated_data):
                    # quest  , new quest 
        instance.content = validated_data.get("content" ,instance.content )
        if "question_type" in validated_data:
            instance.question_type =QuestionType.get_type(validated_data["question_type"])
        instance.order = validated_data.get("order" ,instance.order)
        instance.required = validated_data.get("required" ,instance.required)
        if instance.is_valid():
            instance.save()
            return instance
        raise Exception("Can't update Question , please check")
    

class ChoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choise
        fields = '__all__' 

"""
 json body to create or edit survey with question looks like : 

{
    "name" : "test 123" , 
    end_at : "2023-11-03T12:00:00Z", 
    "is_published":"false",
    "id_deleted":"false",
    "paused":"false",
    questions: [
        {
            id:1, 
            content,
            order,
            required,
            type
        },
        {},
        {}, ......
    ]
}

"""
class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = BaseSurvey
        fields = '__all__' 

    def create(self,validated_data):
        question_data = validated_data.pop("questions")
        survey = BaseSurvey.objects.create(**validated_data)
        for question in question_data:
            Question.objects.create(survey=survey , **question)
        return survey
    
    def update(self, instance, validated_data):
        #### need to fix 
        questions = validated_data.pop("questions")
        survey = BaseSurvey(**validated_data)
        instance.copy_survey(survey)
        instance.question_set.all().delete()
        for question in questions:
            instance.question_set.create(**question)
        return instance

        
        

    
     