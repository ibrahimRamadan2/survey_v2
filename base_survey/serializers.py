from rest_framework import serializers 
from base_survey.models import BaseSurvey , Question , Choise
import datetime
           

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =Choise 
        exclude = ('question', )
    

class QuestionSerialzer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)  

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choise.objects.create(question= question , **choice)
        return question
    
    class Meta:
        model = Question
        exclude = ('survey', )

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerialzer(many=True, required=False)

    def create_questions(self ,survey , questions):
        for question in questions:
            choices = question.pop("choices")
            question = Question.objects.create(survey=survey ,**question)
            for choice in choices:
                Choise.objects.create(question=question , **choice)
        
    def create(self, validated_data):
        questions = validated_data.pop("questions")
        survey = BaseSurvey.objects.create(**validated_data)
        self.create_questions(survey , questions)
        return survey
 
    def update(self, instance ,validated_data):
        try:
            questions = validated_data.pop("questions")
            instance.questions.all().delete()
            self.create_questions(instance , questions)
            instance.save()
            print(instance)
            return instance
        except Exception as e :
            print(e)

    

    class Meta:
        model = BaseSurvey
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
 
        

    
     