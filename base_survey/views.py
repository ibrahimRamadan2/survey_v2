from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import SurveySerializer
from .models import BaseSurvey , Question
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.



class Survey(APIView):
    def get(self, request): # return list of all surveys
        try:
            # import pdb
            # pdb. set_trace() 
            surveys = BaseSurvey.objects.all()
            survey_serializer=  SurveySerializer(surveys , many=True)
            return Response(survey_serializer.data, status= status.HTTP_200_OK)
        except:
            return Response({"error": survey_serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

    def post(self , request):
        """
            {
                "name":"test" ,
                paused:"bool" (optional default=false),
                "end_at":"2023-08-13 05:47:20",
                "published_at":"2023-08-13 05:47:20",
                is_deleted:"false:,
                questions:[
                    {
                        "content":"my first survey",
                        "question_type":"MCQ",
                        "order":1,      // this mean that this is the first question to sort them in frontend. 
                        "required":"True" // this mark the question is not optional 
                        choices:[
                            {
                                content:"egypt"
                            },
                            {},
                            {},
                            ....
                        ]
                    },
                    {},
                    ..
                    ..

                ]
            }
        """
        # import pdb
        # pdb. set_trace()
        survey_serializer = SurveySerializer(data = request.data)

        if survey_serializer.is_valid():
            survey_serializer.save() 
            return Response(survey_serializer.data , status=status.HTTP_201_CREATED)
        return Response({"error":survey_serializer.errors} , status=status.HTTP_400_BAD_REQUEST)
class SurveyDetails(APIView):

    def get(self, request , id):
        survey = get_object_or_404(BaseSurvey, id = id)
        survey_serializer = SurveySerializer(survey)
        return Response(survey_serializer.data , status=status.HTTP_200_OK)
    

    def put(self , request,id):
        survey = get_object_or_404(BaseSurvey, id = id)
        survey_serializer = SurveySerializer(survey , data=request.data)
        if survey_serializer.is_valid():
            survey_serializer.save() 
            return Response(survey_serializer.data , status=status.HTTP_200_OK)
        return Response({"error":f"something wrong while deteting survey"} , status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , id ):
        survey = get_object_or_404(BaseSurvey, id = id)
        survey_serializer = SurveySerializer(survey)
        try:
            survey.delete()
            return Response(survey_serializer.data , status=status.HTTP_200_OK)
        except:
            return Response({"error":f"something wrong while deteting survey"} , status=status.HTTP_400_BAD_REQUEST)


