from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import SurveySerializer
from .models import BaseSurvey
from rest_framework import status
# Create your views here.


class survey(APIView):
    def get(self , request) : 
       surveys = BaseSurvey.objects.all()
       surveys = SurveySerializer( surveys , many = True)
       return Response({"msg" : surveys.data} , status=status.HTTP_200_OK) 
       
    def post(self,  request):
        survey_serializer = SurveySerializer(data =request.data)
        if(survey_serializer.is_valid()):
            survey_serializer.save()
            return Response({"msg" : survey_serializer.data} , status=status.HTTP_200_OK) 
        else:
            return Response({"msg" : survey_serializer.errors} , status=status.HTTP_200_OK)  

