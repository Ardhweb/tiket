from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import TaskSerializer
from task.models import Task
from accounts.models import User
from django.shortcuts import get_object_or_404

class TaskView(APIView):
    
    
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'Task is not found!'},status=status.HTTP_404_NOT_FOUND)

    
    @swagger_auto_schema(
        operation_description="- Fetches all tasks assigned to a particular user.  endpoint:api/tasks?user_email=user-email@.com",
        responses={200: "Return specific user related task list which email we pass thorugh url parameter via GET Method.",
        400:"When user email does'nt provide you  got this 400 error."}
    )
    def get(self, request, *args, **kwargs):
        user_email = request.query_params.get('user_email', None)
        if user_email: 
            try:
                user = User.objects.get(email=user_email)
                #tasks  = Task.objects.filter(users__email=user_email)
                tasks = user.tasks.all()
            except User.DoesNotExist:
                tasks = Task.objects.none()
        elif not user_email:
            return Response({"error": "User email is required"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            tasks = Task.objects.none()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="API to  create a new task , Allows the creation of new tasks with a name and description. endpoint:api/tasks",
        responses={201: "POST method to create an new task , pass the name , desc, status, task_type parameter into  body  with this request.",
        400:"error"}
    )
    def post(self,request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="-API to massign task to  one or multiple users. Enables assigning a task to one or multiple users. endpoint:api/tasks/task_id",
        responses={201: "PUT method to add users to  task or update its attributes , pass the primary_key id to  find the task , pass the name , desc, status, task_type parameter into  body  with this request.",
        400:"error"}
    )
    def patch(self,request,pk):
        task =  self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
        

  
