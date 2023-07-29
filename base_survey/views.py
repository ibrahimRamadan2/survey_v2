from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import SurveySerializer
from .models import BaseSurvey
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.


class Surveys(APIView):
    def get(self , request) : 
       surveys = BaseSurvey.objects.all()
       surveys = SurveySerializer( surveys , many = True)
       return Response({"data" : surveys.data} , status=status.HTTP_200_OK) 
    
    def post(self,  request):
        survey_serializer = SurveySerializer(data=request.data)
        if(survey_serializer.is_valid()):
            survey_serializer.save()
            return Response({"data" : survey_serializer.data} , status=status.HTTP_200_OK) 
        else:
            return Response({"error" : survey_serializer.errors} , status=status.HTTP_200_OK)  

class SurveyDetails(APIView):

    def get(self, request , id: int ):
        survey = get_object_or_404(BaseSurvey,id=id )
        survey = SurveySerializer(survey)
        ## should return survey with questions 
        # each question has a choises ,  and on correct answer
        
        return Response({"data" : survey.data} , status = status.HTTP_200_OK)
    
    def put(self , request , id ):
        survey = get_object_or_404(BaseSurvey,id=id)
        if survey.is_published:
            return Response({"error" : "you can't edit the survey after it has been published"} , status=status.HTTP_403_FORBIDDEN)
        data = request.data 
        serializer = SurveySerializer(survey, data=data)
        if serializer.is_valid() : 
            serializer.save() 
            return Response({"data":serializer.data} , status=status.HTTP_200_OK)
        return Response({"error":serializer.errors} , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , id ):
        survey = get_object_or_404(BaseSurvey,id=id )
        survey.delete() 
        return Response({"data": "survey is deleted successfully"} , status=status.HTTP_200_OK)
    


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
 
    

