from rest_framework.response import Response
from .serializers import AnswerSerializer
from .models import Answer ,Respondant ,BaseSurvey
from rest_framework.views import APIView
from .serializers import AnswerSerializer
from rest_framework.status import * 
from rest_framework import status



class AnswerView(APIView):
    def post(delf ,request):
        answer_serializer =  AnswerSerializer(data = request.data , many=True)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response({"data":"answer submitted successfully"}, status=HTTP_201_CREATED)
        else :
            return Response({"error":answer_serializer.errors}, status=HTTP_400_BAD_REQUEST)


class AnswerDetailsView(APIView):
    """
        should return statistics 
        - total num of responses .. 
        - for each question :
            - return each choice with :
                - how many people choose it (if question tpye is MCQ, [True or false])
                - if answer is just a text then return all answers in a list, (coming soon ....)
        
    """
    """ 
        Json Body
        {
            total_responses:123123 ,
            questions = {
                choices:[
                    {

                    },
                    {}
                ]
            }
        }
    """

    def get(delf ,request,survey_id):
        survey= BaseSurvey.objects.get(id = survey_id)
        total_responses_count = Respondant.objects.filter(survey_id=survey_id).count()
        result=[]
        questions=  survey.questions.all()
        for question in questions:
            question_data={
                "id":question.id ,
                "name":question.content
                }
            choices = question.choices.all()
            for choice in choices:
                question_data[choice.id]= {
                    "count": Answer.objects.filter(choice_id=choice.id).count(),
                    "content":choice.content
                }
                     
            result.append(question_data)
        data = {
            "total_responses_count":total_responses_count,
            "questions":result
        }
        print("##################")
        print("##################")
        print(data)
        print("##################")
        print("##################")
        return Response(data ,status.HTTP_200_OK)
            

    

