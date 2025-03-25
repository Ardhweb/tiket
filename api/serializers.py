from task.models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model() 

class TaskSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='email' , # Fetch emails instead of IDs
        
    )
    class Meta:
        model  = Task
        fields = '__all__'
   