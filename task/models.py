from django.db import models
from accounts.models import User
# Create your models here.

#Table Schema Design for Task.
class Task(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("pending", "Pending"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
        ("on_hold", "On Hold"),
        ("failed", "Failed"),
    )
    TYPE_CHOICES = (
        ("bug", "Bug"),
        ("feature", "Feature"),
        ("improvement", "Improvement"),
        ("task", "Task"),
    )

    name = models.CharField(max_length=20, blank=False, null=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, blank=True, null=True, choices=STATUS_CHOICES)
    task_type = models.CharField(max_length=20, blank=False, null=True,choices=TYPE_CHOICES)
    users = models.ManyToManyField(User, related_name="tasks")  # Many-to-Many
    

    
