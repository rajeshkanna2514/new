from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError 
from .models import User,TaskModel
from .serializers import RegisterSerializer,LoginSerializer,TaskCreateSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):

    def post(self,request,format=None):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            tokens=get_tokens_for_user(user)
            response_data = {
                'user':serializer.data,
                'msg':'Register Successfully',
                'token':tokens
            } 
            return Response(response_data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    permission_classes=[]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            tokens = get_tokens_for_user(user)
            return Response({'token': tokens,"msg":"login success"}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request):
        try:
            refresh_token = request.data("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class TaskManagementView(APIView):
    
    def post(self,request,format=None):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Task Created",status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def get(self, request, format=None):
        try:
            tasks = TaskModel.objects.all()
            serializer = TaskCreateSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            serializer = TaskCreateSerializer(data=request.data)
            serializer.is_valid()  
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
        
class TaskManagementViewId(APIView):   
    
    def put(self, request,id=None, format=None):
        task = TaskModel.objects.get(id=id)
        serializer = TaskCreateSerializer(task, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Task Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id=None,format=None):
        task = TaskModel.objects.get(id=id)
        serializer = TaskCreateSerializer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request,pk=None):
        task = TaskModel.objects.get(id=pk)
        task.delete()
        return Response("Deleted", status=status.HTTP_200_OK)
        
class TaskstatusFilter(viewsets.ModelViewSet):
    queryset=TaskModel.objects.all()
    serializer_class=TaskCreateSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=["taskstatus", "deadline"]
    search_fields =["taskname"] 
    ordering = ["completed_on"]

    