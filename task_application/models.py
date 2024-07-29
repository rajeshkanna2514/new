from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime,timedelta
# Create your models here.

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,unique=True,db_index=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    
class TaskModel(models.Model):
    STATUS_CHOICES = [
            ('applied', 'Applied'),
            ('processing', 'Processing'),  
            ('completed', 'Completed'),
        ]
    STATUS_CHOICES2 = [
            ('high', 'High'),
            ('medium', 'Medium'),  
            ('low', 'Low'),
        ]
    task_assigned = models.ForeignKey(User,null= True,on_delete=models.SET_NULL)    
    username = models.CharField(max_length=255,null=True)
    taskname = models.CharField(max_length=250,null=True,blank=True)
    description = models.TextField()
    taskstatus = models.CharField(max_length=11,
        choices=STATUS_CHOICES,
        default='applied')
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon= models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    completed_on = models.BooleanField(default=False)
    priority = models.CharField(max_length=10,choices=STATUS_CHOICES2,default='Medium')

    def __str__(self):
        return self.taskname or self.username
    
    def mark_as_completed(self):
        self.taskstatus = 'completed'
        self.completed = True
        self.save()

    def task_assign(self, user):
        self.task_assigned = user
        self.save()


